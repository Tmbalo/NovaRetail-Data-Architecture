# Naming Conventions
## Objective
Ensure consistent, clear naming for datasets, tables, pipelines, and scripts to support governance and collaboration.

## General Rules
- Use lowercase with underscores (e.g., `raw_orders`).
- Prefix with layer or purpose (e.g., `bronze_`, `silver_`, `gold_`).
- Include project context (`novaretail`) where applicable.
- Avoid special characters or spaces.

## Datasets (Azure Data Lake)
- **Bronze**: `bronze_<source>_<dataset>`
  - Examples: `bronze_sqlserver_orders`, `bronze_mongodb_clickstream`, `bronze_csv_inventory`.
- **Silver**: `silver_<source>_<dataset>`
  - Examples: `silver_cleaned_orders`, `silver_cleaned_clickstream`, `silver_cleaned_inventory`.
- **Gold**: `gold_<table>`
  - Examples: `gold_sales_fact`, `gold_customer_dim`.

## Tables (Azure Synapse Analytics)
- **Schema**:  `<project>`
    - Example: `novaretail`
- **Fact Tables**: `<schema>.fact_<entity>`
  - Example: `novaretail.fact_sales`.
- **Dimension Tables**: `<schema>.dim_<entity>`
  - Examples: `novaretail.dim_customer`, `novaretail.dim_product`.

## Pipelines (Azure Data Factory)
- Format: `<project>_pipeline_<source>_<layer>`
  - Examples: `novaretail_pipeline_sqlserver_bronze`, `novaretail_pipeline_mongodb_silver`.

## Scripts
- **Python**: Descriptive names (e.g., `bronze_to_silver.py`, `validate_data.py`).
- **SQL**: Descriptive names (e.g., `star_schema.sql`, `create_tables.sql`).

## Airflow DAGs
- Format: `<project>_dag_<purpose>`
  - Example: `novaretail_dag_elt_pipeline`.

## Notes
- Aligned with Epic 1 (data sources: sqlserver, mongodb, csv) and Epic 2 (Medallion Architecture).
- Supports GDPR by tagging PII fields (e.g., `email_pii`) in naming conventions.