# 📣 Stakeholder Request Summary

## 1. Retail Ops Manager (Sibongile)

> "I need real-time alerts when stock falls below reorder levels, and I want to see daily sales by store and region."

**Implication:**  
- Build Gold layer fact tables with stock levels  
- Dashboard with conditional alerts using Power BI  
- Data latency < 15 mins

---

## 2. Marketing Lead (Lebo)

> "We want to track the customer journey from click to purchase, especially which campaigns lead to high-converting traffic."

**Implication:**  
- Integrate clickstream + transaction data in Silver Layer  
- Enrich customer dimension with behavior metrics  
- Funnel visualization in Power BI

---

## 3. CIO (Hendrik)

> "Make sure we're GDPR-compliant. No raw PII should be exposed, and we need full data lineage."

**Implication:**  
- Mask or anonymize sensitive data in Bronze/Silver  
- Use Purview for data catalog and lineage  
- Document all data access roles
