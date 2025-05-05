CREATE TABLE weather_logs (
    id SERIAL PRIMARY KEY,
    station_id VARCHAR(50),
    temperature DECIMAL(5,2),
    humidity DECIMAL(5,2),
    timestamp TIMESTAMP
);
