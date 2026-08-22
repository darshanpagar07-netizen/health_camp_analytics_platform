# Requirements Traceability Matrix (RTM) — Health Camp Analytics Platform

| BR ID  | Epic                                             | Feature                                    | User Story                                            | Test Case ID | Dashboard/Table |
|---|--- |---|---|---|---|
| BR-001 | Epic 1: Standardized Multi-Vendor Data Ingestion | Feature 1.1: Bronze Layer Ingestion        | US-1.1.1: Raw vendor files landed with metadata       | TC-01        | bronze.vendor_a_raw, bronze.vendor_b_raw, bronze.vendor_c_raw |
| BR-001 | Epic 1: Standardized Multi-Vendor Data Ingestion | Feature 1.2: Vendor Format Standardization | US-1.2.1: All 3 vendors mapped to one schema          | TC-02        | silver_health_checkup_clean |
| BR-002 | Epic 2: Data Quality & Governance                | Feature 2.1: Data Quality Flagging         | US-2.1.1: Outlier/suspect readings flagged            | TC-03        | silver_health_checkup_clean (data_quality_flag) |
| BR-003 | Epic 2: Data Quality & Governance                | Feature 2.2: Company SCD2 Tracking         | US-2.2.1: Company attribute history preserved         | TC-04        | silver_company_dim_scd2 |
| BR-004 | Epic 3: Business Reporting                       | Feature 3.1: Company-wise KPI Dashboard    | US-3.1.1: Company health KPIs visualized              | TC-05        | gold.company_summary → Power BI Dashboard 1 |
| BR-005 | Epic 3: Business Reporting                       | Feature 3.2: Camp Performance Dashboard    | US-3.2.1: Camp financial performance visualized       | TC-06        | gold.camp_performance → Power BI Dashboard 2 |
| BR-006 | Epic 3: Business Reporting                       | Feature 3.3: Device Maintenance Dashboard  | US-3.3.1: Device service status visualized            | TC-07        | gold.device_maintenance → Power BI Dashboard 3 |
| BR-007 | Epic 1: Standardized Multi-Vendor Data Ingestion | Feature 1.2: Vendor Format Standardization | US-1.2.1 (extension): BP flag derived from thresholds | TC-08        | silver_health_checkup_clean (bp_flag) |

*(8 rows — every BR-### from the BRD is traced through to a Dashboard or Table, with a linked Test Case.)*