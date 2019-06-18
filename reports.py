import pandas as pd
import datetime as dt

def today(df):
    df_today = df[df.date == str(pd.to_datetime("today").date())]
    hours_spent(df_today)

def week(df):
    last_week_date = pd.to_datetime("today") - pd.to_timedelta("7 days")
    df_week = df[df.date >= str(last_week_date.date())]
    hours_spent(df_week)

def hours_spent(df):
    for grp, data in df.groupby("date"):
        hours = str(dt.timedelta(
            seconds=((data.exit - data.enter).sum().total_seconds())))
        print(f"Hours spent on {grp} : {hours}")
