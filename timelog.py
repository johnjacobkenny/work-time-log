import pandas as pd
import datetime as dt
from os import path

import utils

LOG_FILENAME = "log.csv"
LOG_FILEPATH = path.join(path.dirname(__file__), LOG_FILENAME)
now = pd.to_datetime("today")

def generate_report(df):
    todays_log = df[df.date == str(pd.to_datetime("today").date())]
    hours = str(dt.timedelta(
        seconds=((todays_log.exit - todays_log.enter).sum().total_seconds())))
    print(f"Hours spent today: {hours}")


data = utils.load_data(LOG_FILEPATH)
isClockingIn = not pd.isnull(data.exit.iloc[-1])
if isClockingIn:
    print("Clocking in")
    data = data.append(
        {"date": now.date(), "enter": now}, ignore_index=True)
else:
    print("Clocking out")
    data.exit.iloc[-1] = now

generate_report(data)
utils.save_data(data, LOG_FILEPATH)

