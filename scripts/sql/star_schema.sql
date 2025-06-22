
/*
    NovaRetail Data Warehouse Star Schema
    This script creates a star schema for the NovaRetail data warehouse.
    It includes dimension tables for customers, products, warehouses, regions, and time,
    and a fact table for sales transactions.
    
    The schema is designed for use in Azure Synapse Analytics with a focus on performance and scalability.

    First create a dedicated SQL pool (novaretail_analytics_warehouse) in Azure Synapse Analytics.
    Then run this script to create the star schema.

*/
-- Create schema
CREATE SCHEMA novaretail;
GO

-- Create dimension tables
IF OBJECT_ID('novaretail.dim_customer', 'U') IS NOT NULL
    DROP TABLE novaretail.dim_customer;
GO
CREATE TABLE novaretail.dim_customer (
    customer_id INT NOT NULL,
    customer_name VARCHAR(100),
    email_pii VARCHAR(100),
    phone_pii VARCHAR(50),
    region VARCHAR(50),
    is_pii BIT DEFAULT 1,
    CONSTRAINT pk_customer PRIMARY KEY NONCLUSTERED (customer_id) NOT ENFORCED
)
WITH 
(
    DISTRIBUTION = HASH(customer_id),
    CLUSTERED COLUMNSTORE INDEX
);


IF OBJECT_ID('novaretail.dim_product', 'U') IS NOT NULL
    DROP TABLE novaretail.dim_product;
GO
CREATE TABLE novaretail.dim_product (
    product_id INT NOT NULL,
    product_name VARCHAR(100),
    product_category VARCHAR(50),
    unit_price DECIMAL(10,2),
    CONSTRAINT pk_product PRIMARY KEY NONCLUSTERED (product_id) NOT ENFORCED
)
WITH 
(
    DISTRIBUTION = HASH(product_id),
    CLUSTERED COLUMNSTORE INDEX
);

IF OBJECT_ID('novaretail.dim_warehouse', 'U') IS NOT NULL
    DROP TABLE novaretail.dim_warehouse;
GO
CREATE TABLE novaretail.dim_warehouse (
    warehouse_id INT NOT NULL,
    warehouse_name VARCHAR(50),
    warehouse_region VARCHAR(50),
    employee_count INT,
    CONSTRAINT pk_warehouse PRIMARY KEY NONCLUSTERED (warehouse_id) NOT ENFORCED
)
WITH 
(
    DISTRIBUTION = HASH(warehouse_id),
    CLUSTERED COLUMNSTORE INDEX
)

IF OBJECT_ID('novaretail.dim_region', 'U') IS NOT NULL
    DROP TABLE novaretail.dim_region;
GO
CREATE TABLE novaretail.dim_region (
    region_id INT NOT NULL,
    region_name VARCHAR(50),
    country VARCHAR(50),
    CONSTRAINT pk_region PRIMARY KEY NONCLUSTERED (region_id) NOT ENFORCED
)
WITH 
(
    DISTRIBUTION = REPLICATE,
    CLUSTERED COLUMNSTORE INDEX
);

IF OBJECT_ID('novaretail.dim_time', 'U') IS NOT NULL
    DROP TABLE novaretail.dim_time;
GO
CREATE TABLE novaretail.dim_time (
    date DATE NOT NULL,
    year INT,
    quarter INT,
    month INT,
    day INT,
    CONSTRAINT pk_time PRIMARY KEY NONCLUSTERED (date) NOT ENFORCED
)
WITH 
(
    DISTRIBUTION = REPLICATE,
    CLUSTERED COLUMNSTORE INDEX
);


IF OBJECT_ID('novaretail.fact_sales', 'U') IS NOT NULL
    DROP TABLE novaretail.fact_sales;
GO
-- Create fact table
CREATE TABLE novaretail.fact_sales (
    order_id INT NOT NULL,
    customer_id INT,
    product_id INT,
    warehouse_id INT,
    region_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    CONSTRAINT pk_sales PRIMARY KEY NONCLUSTERED (order_id) NOT ENFORCED
)
WITH 
(
    DISTRIBUTION = HASH(order_id),
    CLUSTERED COLUMNSTORE INDEX
);