import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# connecting Python and PostgreSQL
load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as conn:
    print("PostgreSQL connected successfully!")

query = """
SELECT *
FROM analytics.fact_demand
"""

df = pd.read_sql(query, engine)

print(df.shape)
print(df.head())

# Defining iindependent and dependent variable
X = df[
    [
        "pickup_hour",
        "pickup_weekday",
        "pickup_month",
        "weekend_flag"
    ]
]

y = df["total_rides"]

# Spliting the data in Train and Test Samples

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Training the data wwith RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Model  Evaluation
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred)**0.5)
print("R2:", r2_score(y_test, y_pred))

# Feature Importance
importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

importance = pd.DataFrame({"feature": X.columns, "importance": model.feature_importances_ })

print(importance.sort_values(by="importance", ascending=False))


importance.to_csv(
    "outputs/feature_importance.csv",
    index=False
)

results = pd.DataFrame({
    "actual_demand": y_test.reset_index(drop=True),
    "predicted_demand": y_pred
})

results.to_csv(
    "outputs/predictions.csv",
    index=False
)

# Visualizing actual and Predicted Demand
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.7
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

plt.xlabel("Actual Demand")
plt.ylabel("Predicted Demand")
plt.title("Actual vs Predicted Ride Demand")

plt.savefig(
    "outputs/actual_vs_predicted.png",
    bbox_inches="tight"
)

plt.show()

# Saving built model
import os
import joblib

os.makedirs("model", exist_ok=True)

joblib.dump(
    model,
    "model/demandforecasting_rf.pkl"
)

print("Model saved successfully!")

print(results.head())
# Loading the results to forecast_results table in analytics schema
results.to_sql(
    "forecast_results",
    con=engine,
    schema="analytics",
    if_exists="replace",
    index=False
)

print("Forecast results loaded successfully!")
