End-to-End Azure Data Engineering Project
Project Overview

Designed and implemented an end-to-end Azure Data Engineering pipeline using Azure Synapse Analytics, Azure Data Lake Storage Gen2 (ADLS Gen2), PySpark, and SQL to process retail transaction data following the Medallion Architecture (Bronze, Silver, Gold layers).

Project Workflow
1. Raw Data Ingestion
Collected detailed retail transaction data in JSON format.
Ingested the raw JSON data into Azure Data Lake Storage Gen2.
Converted and stored the data in Parquet format for optimized storage and faster query performance.

2. Bronze Layer – Raw Data Storage
Loaded the raw data into the Bronze layer using PySpark scripts in Azure Synapse Analytics.
Maintained the complete dataset without applying any filtering or transformations.
Preserved the raw transactional data for auditability and future reprocessing requirements.

3. Silver Layer – Data Cleansing and Filtering
Applied business logic in the Silver layer to filter only purchase-related transaction records.
Removed unnecessary or irrelevant transaction types to prepare curated datasets for downstream analytics.
Improved data quality and usability for analytical processing.

4. Gold Layer – Business Aggregations
Performed transformations and aggregations on the curated Silver layer data.
Calculated:
Daily Total Revenue
Daily Total Purchase Count
Prepared business-ready analytical datasets optimized for reporting and dashboarding purposes.

5. SQL Reporting Layer
Loaded the final transformed Gold layer data into a SQL table.
Enabled end users, analysts, and reporting tools to query the processed business data efficiently using SQL queries.
Built a structured reporting layer for easy consumption of analytical insights.

Technologies Used
Azure Synapse Analytics
Azure Data Lake Storage Gen2 (ADLS Gen2)
PySpark
SQL

Key Highlights
Implemented scalable lakehouse architecture using Medallion design principles.
Optimized storage and query performance using Parquet format.
Built modular ETL processing using PySpark.
Created business-ready aggregated datasets for analytics and reporting.
Enabled downstream SQL-based reporting for end users and stakeholders.
