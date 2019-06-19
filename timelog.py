import pandas as pd
import click

now = pd.to_datetime("today")

def clock(data):
    isClockingIn = not pd.isnull(data.iat[-1, -1])
    if isClockingIn:
        click.secho("Clocking in", bold = True, fg="green")
        data = data.append(
            {"date": now.date(), "enter": now}, ignore_index=True)
    else:
        click.secho("Clocking out", bold = True, fg="red")
        data.iat[-1, -1] = now
    return data