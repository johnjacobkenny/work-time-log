import pandas as pd
import datetime as dt
import click

def today(df):
    df_today = df[df.date == str(pd.to_datetime("today").date())]
    day_summary(df_today)

def month(df):
    one_month_date = pd.to_datetime("today") - pd.to_timedelta("31 days")
    df_month = df[df.date >= str(one_month_date.date())]
    hours_spent(df_month)

def week(df):
    last_week_date = pd.to_datetime("today") - pd.to_timedelta("7 days")
    df_week = df[df.date >= str(last_week_date.date())]
    hours_spent(df_week)

def hours_spent(df):
    if pd.isnull(df.iat[-1, -1]):
        df.iat[-1, -1] = pd.to_datetime("today")
    for grp, data in df.groupby("date"):
        date = grp.strftime("%d %b (%a)")
        hours = dt.timedelta(
            seconds=((data.exit - data.enter).sum().total_seconds()))
        print(f"{date} - {str(hours)}")
    return hours

def day_summary(df):
    # In time ############### Out time like a progress bar
    # with a percentage perhaps
    # If currently IN, show an estimated out time for 8 hours
    # If currently OUT, show an estimated 

    # blocks of time - start | end | duration
    # whether currently in or out, and the duration of the same
    if df.size == 0:
        click.secho(f"No logging for today", bold = True, fg="red")
        return
        
    in_time = df.iat[0, 1].to_pydatetime().strftime("%I:%M %p")
    try:
        out_time = df.iat[-1, 2].to_pydatetime().strftime("%I:%M %p")
    except:
        out_time = ""
        pass
    hours = hours_spent(df)
    hours_left = (pd.to_timedelta("8 hours") - hours).to_pytimedelta().seconds
    
    time_leave = (pd.to_datetime("today") + pd.to_timedelta("8 hours") - hours).to_pydatetime().strftime("%I:%M %p")
    
    click.secho()
    click.secho(f"{in_time}", bold = True, fg="green")
    click.secho(f"{out_time}", bold = True, fg="red")
    click.secho()
    click.secho()
    click.secho("I have to work for ", nl=False)
    click.secho(f"{hours_left//3600}hrs {(hours_left%3600)//60}mins", bold = True, fg="red")
    click.secho("I can leave at ", nl=False)
    click.secho(f"{time_leave}", bold = True, fg="green")
    click.secho()