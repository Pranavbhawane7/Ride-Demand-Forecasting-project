INSERT INTO analytics.fact_demand
SELECT
    DATE(pickup_datetime) AS demand_date,

    pickup_hour,

    pickup_weekday,

    pickup_month,

    weekend_flag,

    COUNT(*) AS total_rides,

    SUM(total_amount) AS total_revenue,

    AVG(trip_distance) AS avg_trip_distance

FROM staging.stg_trip_data

GROUP BY
    DATE(pickup_datetime),
    pickup_hour,
    pickup_weekday,
    pickup_month,
    weekend_flag;