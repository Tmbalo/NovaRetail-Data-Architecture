# 📊 NovaRetail Sample Data Overview

This document describes the synthetic sample data provided under `/data/sample_data`. These datasets simulate realistic transactional, behavioral, and operational records across multiple source systems for NovaRetail.

---

## 🧾 1. orders.csv

- **Source System**: SQL Server (Transactional System)
- **Row Count**: ~1,000
- **Primary Keys**: `order_id`
- **Relationships**: 
  - `customer_id` → customers.csv
  - `product_id` → products.csv

### Columns:
| Column Name   | Description                  | Example               |
|---------------|------------------------------|-----------------------|
| order_id      | Unique ID for each order     | 100045                |
| customer_id   | Customer placing the order   | CUST_782              |
| product_id    | Product being purchased      | PROD_33               |
| unit_price    | Price per unit               | 149.99                |
| total_amount  | Total transaction value      | 299.98                |
| order_date    | Timestamp of the order       | 2025-06-15 08:24:00   |
| region        | Customer region              | Gauteng               |
| email_pii     | Customer email address       | john@example.com      |
| phone_pii     | Customer contact number      | 0821234567            |

---

## 🧠 2. clickstream.json

- **Source System**: MongoDB Atlas (Web Behavior Logs)
- **Row Count**: ~2,000
- **Primary Keys**: `session_id`
- **Relationships**:
  - `user_id` → customers.csv
  - `product_id` → products.csv

### Sample Fields:
| Field Name             | Description                         |
|------------------------|-------------------------------------|
| user_id                | User who initiated the session      |
| session_id             | Unique session ID                   |
| product_id             | Product viewed                      |
| product_category       | Product category                    |
| page_views             | Number of pages viewed              |
| session_duration_seconds | Total time spent in session       |
| timestamp              | Session start time                  |

---

## 📦 3. inventory.csv

- **Source System**: SFTP via ERP Extract
- **Row Count**: ~200 (Daily Snapshot)
- **Primary Keys**: `product_id` + `warehouse_id`
- **Relationships**:
  - `product_id` → products.csv

### Columns:
| Column Name     | Description                    |
|------------------|-------------------------------|
| product_id       | Product in inventory           |
| product_name     | Name of the product            |
| product_category | Product category               |
| warehouse_id     | Unique ID for the warehouse    |
| warehouse_name   | Name of warehouse              |
| warehouse_region | Region of the warehouse        |
| stock_quantity   | Current stock available        |
| update_date      | Date snapshot was taken        |
| employee_count   | Staff assigned to warehouse    |
| unit_price       | Per unit cost                  |

---

## 🧍 4. customers.csv

- **Source System**: CRM Master Data
- **Row Count**: ~500
- **Primary Keys**: `customer_id`

### Columns:
| Column Name   | Description                |
|---------------|----------------------------|
| customer_id   | Unique customer ID         |
| customer_name | Full name                  |
| email_pii     | Email address (PII)        |
| phone_pii     | Phone number (PII)         |
| region        | Customer's region          |

---

## 🛒 5. products.csv

- **Source System**: Product Master
- **Row Count**: ~40
- **Primary Keys**: `product_id`

### Columns:
| Column Name     | Description                |
|------------------|---------------------------|
| product_id       | Unique product ID         |
| product_name     | Product name              |
| product_category | Category (e.g., Electronics, Clothing) |

---

## 🔗 Relationship Summary

```plaintext
orders.csv
├── customer_id → customers.csv
└── product_id → products.csv

clickstream.json
├── user_id → customers.csv
└── product_id → products.csv

inventory.csv
└── product_id → products.csv


Prepared by: Thozamile Mbalo
Role: Data Solutions Architect
