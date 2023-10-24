# CLI Example

Quick example to show how a standalone CLI can conditionally reference plugins of multiple types.  

## Plugin

The *./plugin* subdirectory contains a simple package representing an external plugin library with two concrete implementations.  

## CLI

The *./cli* subdirectory contains the CLI entrypoint. It defines a *click* CLI and conditionally defines a *plugin* subcommand that allows the user to execute a plugin if the library is installed.  

The */plugins* subdirectory contains an example plugin that extends *plugin.AbstractClass*. This folder is dynamically loaded so that the contained plugin is registered at runtime.  

## Running the example

Run the following commands from the project root:  

Install:  

```
> pip install -r requirements.txt
```

Run the default plugin impl:  

```
> cli plugin run
Plugin 1: Concrete 1 Operation 1
```

Run the extended plugin impl:  

```
> cli plugin run --impl PluginExtension
My plugin: Extended operation 1
```
