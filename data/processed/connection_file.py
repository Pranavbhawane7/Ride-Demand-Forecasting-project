import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as conn:
    print("PostgreSQL connected successfully!")

sample_data = pd.read_csv("yellow_trip_data.csv")

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