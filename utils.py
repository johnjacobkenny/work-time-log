import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
    except:
        data = pd.DataFrame({"date": [pd.Timestamp(0)], "enter": [
                            pd.Timestamp(0)], "exit": [pd.Timestamp(0)]})
    finally:
        data.date = data.date.astype('datetime64[ns]')
        data.enter = data.enter.astype('datetime64[ns]')
        data.exit = data.exit.astype('datetime64[ns]')
        return data


def save_data(data, filepath):
    data.date = data.date.astype('datetime64[ns]')
    data.enter = data.enter.astype('datetime64[ns]')
    data.exit = data.exit.astype('datetime64[ns]')
    data.to_csv(filepath, index=None)
