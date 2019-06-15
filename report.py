import pandas as pd
import datetime as dt

def generate(df):
    todays_log = df[df.date == str(pd.to_datetime("today").date())]
    hours = str(dt.timedelta(
        seconds=((todays_log.exit - todays_log.enter).sum().total_seconds())))
    print(f"Hours spent today: {hours}")

