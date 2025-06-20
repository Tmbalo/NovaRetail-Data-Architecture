# Requirements Analysis
## Objective
Build a cloud-native data platform to integrate transactional (SQL Server), clickstream (MongoDB), and inventory (CSV) data for real-time analytics with GDPR compliance.

## Stakeholder Interviews
### 1. Transactional Data (SQL Server – Orders)
- **Owner**: Sales Operations team.
- **Business Process**: Order processing, customer management, sales tracking.
- **Documentation**: Database schema, table metadata available.
- **Data Model/Catalogue**: Logical model exists; partial catalogue.
- **Storage**: SQL Server 2019 on-premises.
- **Integration**: DirectDB (ODBC/JDBC), CSV extracts, REST API.
- **Load Strategy**: Incremental loads by `order_date`, latest 30 days (~10,000 rows/day, 5 MB).
- **Performance**: Use read-only replicas, schedule midnight SAST.
- **Auth**: SQL Server credentials, IP whitelisting.

### 2. Clickstream Data (MongoDB)
- **Owner**: Web Analytics team.
- **Business Process**: Website performance, user behavior analysis.
- **Documentation**: Collection schema in Confluence.
- **Data Model/Catalogue**: No model; basic catalogue.
- **Storage**: MongoDB Atlas on AWS.
- **Integration**: MongoDB API, JSON exports, Kafka.
- **Load Strategy**: Incremental loads by `timestamp`, latest 30 days (~20,000 documents/day, 10 MB).
- **Performance**: Use secondary replicas, schedule off-peak.
- **Auth**: API keys, IP whitelisting.

### 3. Inventory Data (CSV)
- **Owner**: Inventory Management team.
- **Business Process**: Inventory tracking, stock replenishment.
- **Documentation**: CSV schema in OneDrive.
- **Data Model/Catalogue**: None; schema as reference.
- **Storage**: CSV files on SFTP server.
- **Integration**: SFTP file extracts.
- **Load Strategy**: Full loads daily, latest snapshot (~5,000 rows, 2 MB).
- **Performance**: Schedule 2 AM SAST downloads.
- **Auth**: SFTP credentials, SSH keys, optional IP whitelisting.

## Data Sources
- **SQL Server (Orders)**: `order_id`, `customer_id`, `customer_name`, `email_pii`, `phone_pii`, `product_id`, `product_name`, `product_category`, `unit_price`, `order_date`, `total_amount`, `region`.
- **MongoDB (Clickstream)**: `user_id`, `session_id`, `page_views`, `product_id`, `product_name`, `product_category`, `timestamp`, `session_duration_seconds`.
- **CSV (Inventory)**: `product_id`, `product_name`, `product_category`, `unit_price`, `warehouse_id`, `warehouse_name`, `warehouse_region`, `employee_count`, `stock_quantity`, `update_date`.

## Business Questions
- What are the top-selling `product_categories` by `total_amount`?
- Which `customer_names` drive revenue by `region`?
- How does `session_duration_seconds` correlate with `page_views` or `product_id` views?
- Which `warehouse_regions` have low `stock_quantity`?
- How can `email_pii` support GDPR-compliant marketing?

## Data Quality
- **Issues**:
  - Nulls in `email_pii`, `phone_pii`.
  - Duplicates in `order_id`, `session_id`.
  - Invalid `total_amount`, `stock_quantity` (e.g., negative).
  - Incorrect `product_category` (e.g., Sofa in Clothing).
- **Cleansing**:
  - Deduplicate by `order_id`, `session_id`.
  - Impute null `email_pii` with "unknown".
  - Validate `total_amount`, `stock_quantity` ≥ 0.
  - Enforce `product_category` mapping (e.g., Sofa to Furniture).

## Integration
- **Joins**: Orders and inventory on `product_id`; clickstream to orders via `user_id` to `customer_id`.
- **Pipeline**:
  - **Ingestion**: Azure Data Factory for SQL Server (ODBC), MongoDB (JSON exports), CSV (SFTP).
  - **Storage**: Azure Data Lake (Bronze: raw; Silver: cleaned).
  - **Processing**: Databricks (PySpark) for cleansing.
  - **Target**: Azure Synapse Analytics (Gold: star schema).
  - **Orchestration**: Airflow for scheduling.
- **Star Schema**: `fact_sales`, `dim_customer`, `dim_product`, `dim_warehouse`, `dim_region`, `dime_time`.

## Scope
- Focus on latest 30 days; historization optional.
- GDPR compliance for `email_pii`, `phone_pii`.

## Documentation
- Data model, catalogue, dictionary for stakeholders.