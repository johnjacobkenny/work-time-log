import click

import reports
from timelog import clock as clk
from utils import load_data, save_data
from constants import LOG_FILEPATH

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """ This cli allows you to track your work time and also view reports. """
    data = load_data(LOG_FILEPATH)
    ctx.obj = data

    if ctx.invoked_subcommand is None:
        ctx.invoke(reports)

@cli.command()
@click.pass_obj
def clock(data):
    """ Log your start or end time """
    data = clk(data)
    save_data(data, LOG_FILEPATH)

@cli.command()
@click.argument("report_name", required=False)
@click.pass_obj
def report(data, report_name):
    """ View reports 
    
    today (default) - report for today

    week - report for the last week

    month - report for the month
    """
    if report_name == "week":
        reports.week(data)
    else:
        reports.today(data)

if __name__ == "__main__":
    cli(obj={})
