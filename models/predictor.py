from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(df):
    df["day"] = df["date"].dt.dayofyear  # Convert dates to numerical format
    X = df[["day"]].values
    y = df["steps"].values

    model = LinearRegression()
    model.fit(X, y)
    
    return model

def predict_steps(model, future_dates):
    future_days = np.array(future_dates).reshape(-1,1)
    return model.predict(future_days)