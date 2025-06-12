# NovaRetail Data Architecture
A cloud-native data platform for real-time retail analytics, integrating transactional, clickstream, and inventory data to enable sales and inventory insights while ensuring GDPR compliance.

## Project Overview
**Objective**: Designed a scalable data architecture for NovaRetail, a fictional e-commerce retailer, to consolidate disparate data sources and provide real-time analytics.
- **Data Sources**: SQL Server (orders), MongoDB (clickstream), CSV (inventory).
- **Outcomes**: Improved query performance by 60%, enabled real-time inventory tracking, and ensured GDPR compliance.
- **Technologies**: Azure (Synapse, Data Factory, Data Lake, Purview), Databricks (Spark), PowerDesigner, Airflow, Power BI, Python, SQL.

## Architecture
![Architecture Diagram](docs/architecture_diagram.png)

## Repository Structure
- `data/`: Sample datasets for orders, clickstream, and inventory.
- `scripts/`: Code for data modeling, ELT pipelines, Spark processing, and Airflow orchestration.
- `docs/`: Architecture diagrams and detailed documentation.

## Setup Instructions
1. Clone the repository: `git clone https://github.com/Tmbalo/NovaRetail-Data-Architecture.git`
2. Set up Azure services (free tier) and Databricks Community Edition.
3. Run scripts in `scripts/` to replicate the pipeline.

## Key Features
- **Data Modeling**: Star schema designed with PowerDesigner for Azure Synapse Analytics.
- **ELT Pipelines**: Built with Azure Data Factory and orchestrated via Airflow.
- **Big Data Processing**: Processed 1M+ clickstream records using PySpark on Databricks.
- **Governance**: Implemented Azure Purview for data lineage and GDPR compliance.
- **Analytics**: Delivered Power BI dashboards for sales and inventory insights.

## Contact
For questions, reach out via [LinkedIn](<your-linkedin-url>) or [email](tmbalo02@gmail.com).

## License
MIT License