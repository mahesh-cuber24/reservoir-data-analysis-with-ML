
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def train_model(df):
    features = ['rainfall_mm', 'temperature_C', 'inflow_cumecs', 'outflow_cumecs',
                'dayofyear', 'month', 'rolling_net_flow']
    X = df[features]
    y = df['water_level_m']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse:.2f}')
    
    joblib.dump(model, 'model.pkl')
    return model, X_test, y_test, predictions
