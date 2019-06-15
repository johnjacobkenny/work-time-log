import pandas as pd
from os import path

import utils
import report

LOG_FILENAME = "log.csv"
LOG_FILEPATH = path.join(path.dirname(__file__), LOG_FILENAME)
now = pd.to_datetime("today")

data = utils.load_data(LOG_FILEPATH)
isClockingIn = not pd.isnull(data.exit.iloc[-1])
if isClockingIn:
    print("Clocking in")
    data = data.append(
        {"date": now.date(), "enter": now}, ignore_index=True)
else:
    print("Clocking out")
    data.exit.iloc[-1] = now

report.generate(data)
utils.save_data(data, LOG_FILEPATH)

