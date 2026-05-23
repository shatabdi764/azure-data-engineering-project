#!/usr/bin/env python
# coding: utf-8

# ## python code for medallion architecture
# 
# 
# 

# In[5]:


from pyspark.sql.functions import col, to_date, lower
df_bronze = spark.read.parquet("abfss://retail1@pocretail11.dfs.core.windows.net/bronze/shatabdi764/azure-data-engineering-project/refs/heads/main/retail_transactions_bronze.parquet")
df_bronze.show()


# In[6]:


df_silver = (
    df_bronze
    .filter(col("event_type") == "purchase")
    .dropna(subset=["customer_id", "amount"])
    .withColumn("event_date", to_date(col("event_timestamp")))
    .withColumn("payment_method", lower(col("payment_method")))
    .withColumn("amount", col("amount").cast("float"))
    .select(
        "event_id", "customer_id", "event_date", "product_id",
        "product_category", "payment_method", "amount", "location"
    )
)
df_silver.write.mode("overwrite").parquet("abfss://retail1@pocretail11.dfs.core.windows.net/retail/silver/")


# In[9]:


from pyspark.sql.functions import sum, count, col

df_silver = spark.read.parquet("abfss://retail1@pocretail11.dfs.core.windows.net/retail/silver/")

df_silver.show()


# In[11]:


df_daily_revenue = (
    df_silver.groupBy("event_date")
    .agg(sum("amount").alias("daily_revenue"), count("*").alias("total_purchases"))
)

df_daily_revenue.write.mode("overwrite").parquet("abfss://retail1@pocretail11.dfs.core.windows.net/gold/")
df_daily_revenue.show()

