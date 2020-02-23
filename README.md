# AWS Conftest Plugin
A Conftest plugin for validating AWS resources with Open Policy Agent.

## Installation

To install the plugin, you can use the `conftest plugin install command`:

```console
conftest plugin install https://github.com/Blokje5/aws-conftest-plugin.git
```

## Usage

To validate a resource you can specifiy the resource type along with an identifier to the `conftest aws` command.

```console
conftest aws ec2 <ec2-instance-id>
```

Currently, the following resources are supported

- ec2
