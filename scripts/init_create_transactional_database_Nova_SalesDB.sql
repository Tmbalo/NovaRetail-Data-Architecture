USE [master]
GO

/*
=================================================================================
Create Nova_SalesDB Database and load the raw data
=================================================================================

Script Purpose:
	This script creates a new database named 'Nova_SalesDB' after checking if it already exists.
	If the database exists, it is dropped and recreated. Additionally, the script sets up three tables
	within the database: 'customers', 'products', and 'orders'. 

	It will also load the raw data dirty Sales dirty data that was generated (refere to scripts/data_generation)

WARNING!!!:
	Running this script will drop the entire 'Nova_SalesDB' database if it exists.
	All data in the database will be permanetly deleted. Proceed with caution
	and ensure you have proper up-to-date backups before running this script.

*/


-- Drop and recreate the 'Nova_SalesDB' database
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'Nova_SalesDB')
BEGIN
	ALTER DATABASE Nova_SalesDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
	DROP DATABASE Nova_SalesDB;
END

-- Create the Nova_SalesDB database:
CREATE DATABASE [Nova_SalesDB];
GO

-- Create all needed transactional tables (customers, products, and orders)
USE [Nova_SalesDB]
GO

DROP TABLE IF EXISTS [dbo].[customers]
GO
CREATE TABLE [dbo].[customers](
	[customer_id] [nvarchar](50) NOT NULL,
	[customer_name] [nvarchar](50) NOT NULL,
	[email_pii] [nvarchar](50) NULL,
	[phone_pii] [nvarchar](50) NULL,
	[region] [nvarchar](50) NOT NULL,
	[marketing_consent] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO


DROP TABLE IF EXISTS [dbo].[products]
GO
CREATE TABLE [dbo].[products](
	[product_id] [nvarchar](50) NOT NULL,
	[product_name] [nvarchar](50) NOT NULL,
	[product_category] [nvarchar](50) NOT NULL,
	[unit_price] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO




DROP TABLE IF EXISTS [dbo].[orders]
GO
CREATE TABLE [dbo].[orders](
	[order_id] [nvarchar](50) NOT NULL,
	[customer_id] [nvarchar](50) NOT NULL,
	[product_id] [nvarchar](50) NOT NULL,
	[unit_price] [nvarchar](50) NOT NULL,
	[total_amount] [nvarchar](50) NOT NULL,
	[order_date] [nvarchar](50) NOT NULL,
	[region] [nvarchar](50) NOT NULL,
	[email_pii] [nvarchar](50) NULL,
	[phone_pii] [nvarchar](50) NULL
) ON [PRIMARY]
GO



--- Load customers table:

TRUNCATE TABLE dbo.customers;

BULK INSERT dbo.customers
FROM '<insert csv file path and file>'
WITH(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);


--- Load products table:

TRUNCATE TABLE dbo.products;

BULK INSERT dbo.products
FROM '<insert csv file path and file>'
WITH(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);


--- Load orders table:

TRUNCATE TABLE dbo.orders;

BULK INSERT dbo.orders
FROM '<insert csv file path and file>'
WITH(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);