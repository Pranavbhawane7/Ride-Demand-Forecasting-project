import pandas as pd
from sqlalchemy import create_engine

sample_data = pd.read_csv("yellow_trip_data.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:9764283028@localhost:5432/analytics_platform"
)

# Optional verification
print(sample_data.shape)
print(sample_data.head())

# Load into raw layer
sample_data.to_sql(
    "yellow_trip_data",
    con=engine,
    schema="raw",
    if_exists="append",
    index=False
)

print("Data loaded successfully!")