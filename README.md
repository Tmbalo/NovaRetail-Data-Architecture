# 🛒 NovaRetail Data Architecture Project

## 🚀 Project Overview
NovaRetail is a simulated cloud-native data architecture project for a retail business. It demonstrates real-time analytics across transactional, clickstream, and inventory data sources using the Medallion Architecture (Bronze, Silver, Gold) and enterprise-grade governance.

This project reflects the responsibilities of a Data Solutions Architect—covering ingestion, transformation, modeling, governance, and analytics in Azure and Databricks.

---

## 🧱 Architecture

![NovaRetail Architecture](docs/architecture_diagram.png)

- **Bronze Layer:** Raw ingestion of transactional, clickstream, and inventory data
- **Silver Layer:** Cleansed and joined data with standard formats and enhanced quality
- **Gold Layer:** Star schema (fact/dim) model ready for analytics in Synapse and Power BI

---

## 🧰 Tech Stack

| Area | Tools & Tech |
|------|--------------|
| Cloud Platform | Azure |
| Storage | Azure Data Lake |
| Processing | Azure Data Factory, Databricks (Spark), Python |
| Modeling | Azure Synapse Analytics |
| Governance | Azure Purview |
| Orchestration | Airflow |
| Visualization | Power BI |
| Data Generation | Python Faker |

---

## 📁 Repository Structure

NovaRetail-Data-Architecture/
│
├── data_generation/ # Python scripts to generate synthetic source data
├── data_model/ # Star schema DDLs and data modeling artifacts
├── pipelines/ # Notebooks and scripts for Bronze, Silver, Gold
├── docs/ # Architecture diagrams, metadata, governance docs
├── analytics/ # Power BI dashboards and reports
├── governance/ # Data dictionary, GDPR compliance documentation
└── README.md


---

## 📊 Business Use Cases

- **Inventory Forecasting** based on daily transactional trends
- **Clickstream Attribution** to understand product discovery and engagement
- **Product Recommendation Inputs** using customer and product behavior data
- **Real-Time Sales Insights** for marketing and ops teams

---

## 🧪 How to Run

> Pre-reqs: Azure account, Databricks workspace, Power BI Desktop

1. Clone the repo
2. Generate data via `/data_generation/generate_data.py`
3. Load Bronze using notebooks in `/pipelines/bronze_layer`
4. Transform Silver and Gold layers via respective notebooks
5. Connect Power BI to Synapse SQL endpoint
6. View dashboards in `/analytics`

---

## 🔐 Governance & Compliance

- Azure Purview for metadata cataloging
- PII classification on `email`, `phone`
- Access control and lineage documentation in `/governance`

---

## 📈 Sample Outputs

📊 [Click here](analytics/sales_dashboard.pbix) to view the interactive dashboard  
📄 [Sample Data Dictionary](governance/data_dictionary.xlsx)  
🗂️ [ER Diagram](docs/star_schema.png)

---

## 👤 Simulated Stakeholders

- **Retail Ops Manager:** Wants real-time stock alerts & supplier dashboards
- **Marketing Lead:** Seeks customer segmentation and clickstream funnel tracking
- **CIO:** Focused on GDPR compliance, data governance, and security

---

## 📬 Feedback & Collaboration

Pull requests and suggestions welcome!  
Feel free to fork or use for your own architectural learning or interviews.

---

## 📄 License
MIT License