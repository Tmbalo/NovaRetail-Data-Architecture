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
	[CustomerID] [nvarchar](50) NOT NULL,
	[CustomerName] [nvarchar](50) NOT NULL,
	[Email] [nvarchar](50) NULL,
	[Gender] [nvarchar](50) NOT NULL,
	[Phone] [nvarchar](50) NOT NULL,
	[SignupDate] [nvarchar](50) NOT NULL,
	[Region] [nvarchar](50) NOT NULL,
	[LoyaltyPoints] [nvarchar](50) NOT NULL,
	[AccountStatus] [nvarchar](50) NOT NULL,
	[LastLogin] [nvarchar](50) NOT NULL,
	[PreferredLanguage] [nvarchar](50) NOT NULL,
	[PreferredPaymentMethod] [nvarchar](50) NOT NULL,
	[LastPurchaseDate] [nvarchar](50) NOT NULL,
	[Address] [nvarchar](100) NOT NULL
) ON [PRIMARY]
GO

DROP TABLE IF EXISTS [dbo].[products]
GO
CREATE TABLE [dbo].[products](
	[ProductID] [nvarchar](50) NOT NULL,
	[ProductName] [nvarchar](50) NULL,
	[Category] [nvarchar](50) NOT NULL,
	[Price] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO


DROP TABLE IF EXISTS [dbo].[orders]
GO
CREATE TABLE [dbo].[orders](
	[OrderID] [nvarchar](50) NOT NULL,
	[CustomerID] [nvarchar](50) NOT NULL,
	[ProductID] [varchar](50) NOT NULL,
	[Quantity] [nvarchar](50) NOT NULL,
	[TotalAmount] [nvarchar](50) NOT NULL,
	[OrderDate] [nvarchar](50) NULL,
	[region] [nvarchar](50) NOT NULL,
	[PaymentMethod] [nvarchar](50) NOT NULL,
	[OrderStatus] [nvarchar](50) NOT NULL,
	[ShippingAddress] [nvarchar](100) NOT NULL,
	[BillingAddress] [nvarchar](100) NOT NULL,
	[Discount] [nvarchar](50) NOT NULL,
	[Tax] [nvarchar](50) NOT NULL,
	[ShippingCost] [nvarchar](50) NOT NULL,
	[TrackingNumber] [nvarchar](50) NOT NULL,
	[DeliveryDate] [nvarchar](50) NOT NULL,
	[ReturnStatus] [nvarchar](50) NOT NULL,
	[ReturnReason] [nvarchar](50) NOT NULL,
	[Rating] [nvarchar](50) NOT NULL,
	[Review] [nvarchar](150) NOT NULL
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