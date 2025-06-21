# Data Management Approach
## Objective
Build a cloud-native data platform for real-time retail analytics, integrating transactional (SQL Server), clickstream (MongoDB), and inventory (CSV) data with GDPR compliance.

## Chosen Approach
- **Data Warehouse**: Azure Synapse Analytics (**NovaRetail Analytics Warehouse**).
- **Architecture Model**: Medallion Architecture (Bronze, Silver, Gold).

## Justification
- **Medallion Architecture**:
  - **Bronze**: Stores raw data in Azure Data Lake, supporting CSV/JSON formats and scalability for ~1M+ records.
  - **Silver**: Cleanses data in Databricks (PySpark), addressing duplicates, nulls, and category mismatches (e.g., Sofa in Furniture).
  - **Gold**: Star schema in Synapse for real-time analytics (e.g., sales by product_category, low-stock warehouses).
  - **Benefits**: Scalability, governance via Azure Purview, separation of raw and processed data.
- **Azure Synapse Analytics**:
  - Serverless SQL pools for fast queries on large datasets.
  - Integrates with Azure Data Lake, Data Factory, and Purview for end-to-end data flow.
  - Supports star schema for business questions (e.g., customer revenue by region).

## Tools
- **Ingestion**: Azure Data Factory (ODBC for SQL Server, JSON for MongoDB, SFTP for CSV).
- **Processing**: Databricks (PySpark) for transformations.
- **Storage**: Azure Data Lake (Bronze/Silver), Synapse (Gold).
- **Governance**: Azure Purview for PII tagging and lineage.
- **Orchestration**: Apache Airflow for ELT pipelines.
- **Visualization**: Power BI for dashboards.