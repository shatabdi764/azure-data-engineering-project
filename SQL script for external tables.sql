-- sql table

CREATE EXTERNAL DATA SOURCE blob_retail1_datasource
WITH (
    LOCATION = 'https://pocretail11.blob.core.windows.net/retail1'
);


CREATE EXTERNAL FILE FORMAT ParquetFormat
WITH (
    FORMAT_TYPE = PARQUET
);

CREATE EXTERNAL TABLE daily_revenue (
    event_date DATE,
    daily_revenue FLOAT,
    total_purchases INT
)
WITH (
    LOCATION = '/gold/',  -- Important: folder path only
    DATA_SOURCE = blob_retail1_datasource,
    FILE_FORMAT = ParquetFormat
);



select * from daily_revenue