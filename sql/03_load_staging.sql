INSERT INTO staging.stg_trip_data (
    pickup_datetime,
    dropoff_datetime,
    trip_duration_minutes,
    pickup_hour,
    pickup_day,
    pickup_month,
    pickup_weekday,
    weekend_flag,
    trip_distance,
    total_amount,
    passenger_count
)
SELECT
    pickup_datetime,
    dropoff_datetime,

    EXTRACT(EPOCH FROM (
        dropoff_datetime - pickup_datetime
    )) / 60 AS trip_duration_minutes,

    EXTRACT(HOUR FROM pickup_datetime) AS pickup_hour,

    EXTRACT(DAY FROM pickup_datetime) AS pickup_day,

    EXTRACT(MONTH FROM pickup_datetime) AS pickup_month,

    EXTRACT(DOW FROM pickup_datetime) AS pickup_weekday,

    CASE
        WHEN EXTRACT(DOW FROM pickup_datetime) IN (0, 6)
        THEN 1
        ELSE 0
    END AS weekend_flag,

    trip_distance,

    total_amount,

    passenger_count

FROM raw.yellow_trip_data;