import pandas as pd

now = pd.to_datetime("today")

def clock(data):
    isClockingIn = not pd.isnull(data.exit.iloc[-1])
    if isClockingIn:
        print("Clocking in")
        data = data.append(
            {"date": now.date(), "enter": now}, ignore_index=True)
    else:
        print("Clocking out")
        data.exit.iloc[-1] = now
    return data