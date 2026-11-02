CREATE TABLE raw.yellow_trip_data (
    vendor_id INTEGER,
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count NUMERIC,
    trip_distance NUMERIC,
    pickup_longitude NUMERIC,
    pickup_latitude NUMERIC,
    ratecode_id INTEGER,
    store_and_fwd_flag VARCHAR(1),
    dropoff_longitude NUMERIC,
    dropoff_latitude NUMERIC,
    payment_type INTEGER,
    fare_amount NUMERIC,
    extra NUMERIC,
    mta_tax NUMERIC,
    tip_amount NUMERIC,
    tolls_amount NUMERIC,
    improvement_surcharge NUMERIC,
    total_amount NUMERIC
);

CREATE TABLE staging.stg_trip_data (
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    trip_duration_minutes NUMERIC,
    pickup_hour INTEGER,
    pickup_day INTEGER,
    pickup_month INTEGER,
    pickup_weekday INTEGER,
    weekend_flag INTEGER,
    trip_distance NUMERIC,
    total_amount NUMERIC,
    passenger_count NUMERIC
);


CREATE TABLE analytics.fact_demand (
    demand_date TIMESTAMP,
    pickup_hour INTEGER,
    total_rides INTEGER,
    total_revenue NUMERIC,
    avg_trip_distance NUMERIC
);

CREATE TABLE analytics.forecast_results (
    forecast_date TIMESTAMP NOT NULL,

    predicted_demand NUMERIC(10,2) NOT NULL,

    suggested_surge_multiplier NUMERIC(3,2),

    model_name VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);