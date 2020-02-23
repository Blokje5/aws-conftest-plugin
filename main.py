import datetime
import json
import subprocess

import boto3
import click


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


class CLIContext:
    def __init__(self):
        if not self.check_conftest_program():
            raise RuntimeError("Could not find the conftest program")
        self.ctx = {}

    def check_conftest_program(self):
        from shutil import which

        if which("conftest"):
            return True

        return False


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = CLIContext()


@cli.command()
@click.argument("instance_id")
@click.option(
    "--output",
    default=False,
    help="Print the ec2 instance output instead of running a test against it",
)
@click.option("--policy", default="policy", help="path to the policy dir")
@click.pass_context
def ec2(ctx, instance_id, output, policy):
    client = boto3.client("ec2")
    response = client.describe_instances(
        Filters=[{"Name": "instance-id", "Values": [instance_id]}]
    )
    instance = response["Reservations"][0]["Instances"][0]
    if output:
        click.echo(json.dumps(instance, indent=4, default=default))
    else:
        call_conftest(json.dumps(instance, default=default), policy)


def call_conftest(input, policy):
    p = subprocess.Popen(
        ["conftest", "test", "--input", "json", "--policy", policy, "-"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
    )
    output = p.communicate(str.encode(input))[0]
    print(output.decode())


if __name__ == "__main__":
    cli(obj={})
