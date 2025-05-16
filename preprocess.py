
import pandas as pd

def load_and_engineer_features(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['date'])
    df['dayofyear'] = df['date'].dt.dayofyear
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['net_flow'] = df['inflow_cumecs'] - df['outflow_cumecs']
    df['rolling_net_flow'] = df['net_flow'].rolling(window=7, min_periods=1).mean()
    df.dropna(inplace=True)
    return df
