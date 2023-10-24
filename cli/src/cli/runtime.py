import glob
import importlib.util
import os
from pathlib import Path

import click


# simple dynamic import of a module given name and abspath
# see https://stackoverflow.com/a/57892961
def dynamic_import(module_name, path):
    module_spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


# CLI base command
@click.group()
def cli():
    pass


try:
    from plugin import AbstractClass as plugin_factory

    # default the plugin directory to ./plugins - typically
    # this would be ~/.config/myapp/plugins or similar
    DEFAULT_PLUGIN_MODULE = Path(__file__).resolve().parent / "plugins"


    # register the plugin subcommand if the import resolves
    @cli.group()
    def plugin():
        pass


    # nested subcommands to run the plugin etc.
    @plugin.command()
    @click.option('--impl', default="ConcreteClass1", help='Concrete implementation class name.')
    def run(impl):
        # load the plugin modules dynamically. this could happen globally
        # instead depending on how the plugins are configured...
        for module in glob.glob(str(DEFAULT_PLUGIN_MODULE / "*.py")):
            modname = os.path.split(module)[-1].strip(".py")
            globals()[modname] = dynamic_import(modname, module)
        p = plugin_factory.instance(impl)
        p.operation1()

except ImportError:
    print("Skipping plugin command, plugin lib not available")
