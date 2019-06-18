import click

from report import generate
from timelog import clock as clk
from utils import load_data, save_data
from constants import LOG_FILEPATH

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    data = load_data(LOG_FILEPATH)
    ctx.obj = data

    if ctx.invoked_subcommand is None:
        ctx.invoke(report)

@cli.command()
@click.pass_obj
def clock(data):
    data = clk(data)
    save_data(data, LOG_FILEPATH)

@cli.command()
@click.pass_obj
def report(data):
    generate(data)

if __name__ == "__main__":
    cli(obj={})
