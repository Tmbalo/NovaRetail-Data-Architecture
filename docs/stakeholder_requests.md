# 📣 Stakeholder Interview Summary – NovaRetail

This document summarizes the input from simulated stakeholder interviews conducted during the Requirements Analysis phase. It outlines data ownership, technical integration needs, and performance considerations across three core data domains.

---

## 1. 🧾 Transactional Data – SQL Server (Orders)

**Stakeholder**: Sales Operations Team Lead  
**Business Process**: Order processing, customer management, sales tracking  
**Data Owner**: Sales Operations team (Sales IT Group)  

### Key Points:
- Stored in SQL Server 2022 (on-prem).
- Integration via ODBC/JDBC, CSV extracts, and REST API.
- Incremental loads using `order_date`, targeting the last 30 days (~10,000 rows/day).
- Read-only replicas used for performance; scheduled at midnight SAST.
- Authentication via SQL Server credentials with IP whitelisting.

---

## 2. 📊 Clickstream Data – MongoDB

**Stakeholder**: Web Analytics Team Lead  
**Business Process**: Website user behavior, session analysis, marketing attribution  
**Data Owner**: Web Analytics team (Digital IT Group)  

### Key Points:
- Stored in MongoDB Atlas (AWS-hosted).
- Integration via MongoDB API, JSON exports, and Kafka (streaming optional).
- Incremental loads using `timestamp`, last 30 days (~20,000 docs/day).
- Secondary read replicas for performance; off-peak scheduling.
- Authentication via API keys; IP whitelisting required.

---

## 3. 🏬 Inventory Data – CSV on SFTP

**Stakeholder**: Inventory Management Team Lead  
**Business Process**: Stock tracking, warehouse operations  
**Data Owner**: Inventory Management team (Supply Chain IT Group)  

### Key Points:
- Stored as daily CSV snapshots on an SFTP server.
- No historical loads — full snapshot each day (~5,000 rows, ~2MB).
- Integration only via SFTP.
- Bandwidth constraints; download at 2 AM SAST.
- Auth via SFTP credentials and SSH keys; optional IP whitelist.

---

## 📌 Summary of Integration Considerations

| Source         | Storage        | Load Type   | Frequency | Size        | Auth Method        |
|----------------|----------------|-------------|-----------|-------------|--------------------|
| SQL Server     | On-prem        | Incremental | Daily     | ~10k rows    | SQL creds + IP     |
| MongoDB Atlas  | AWS (cloud)    | Incremental | Daily     | ~20k docs    | API keys + IP      |
| CSV (Inventory)| SFTP           | Full        | Daily     | ~5k rows     | SSH/SFTP + IP opt. |

---

## 🧠 Design Implications
- All data sources must align to a 30-day scope for analytics.
- Data pipelines should run in the early morning hours to avoid business-hour system strain.
- Integration patterns vary and require connectors: ODBC for SQL, JSON loader for MongoDB, and SFTP polling for CSV.

---

## 🔐 GDPR & Data Governance
- `email_pii` and `phone_pii` must be masked or anonymized.
- Metadata and lineage will be catalogued in Azure Purview.

---

*Prepared by: Thozamile Mbalo  
Role: Data Solutions Architect*  
