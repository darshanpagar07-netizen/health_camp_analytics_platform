# UAT Test Cases — Health Camp Analytics Platform

## TC-01: Bronze Layer Ingestion Metadata
**Precondition:** A new vendor file is available in the Databricks Volume
**Steps:**
1. Run the Bronze ingestion notebook
2. Query the resulting Bronze table
**Expected Result:** File is appended (never overwritten) to its Bronze table with `ingestion_ts` populated
**Actual Result:** _[To be filled Day 17]_
**Status:** _[Pending]_

## TC-02: Vendor Format Standardization
**Precondition:** Bronze tables exist for Vendor A, B, and C
**Steps:**
1. Run the Silver standardization notebook
2. Query `silver_health_checkup_clean`
**Expected Result:** A single table exists with consistent column names (employee_id, camp_id, bp_systolic, bp_diastolic, sugar_fasting, bmi) across all 3 vendors
**Actual Result:** _[To be filled Day 17]_
**Status:** _[Pending]_

## TC-03: Data Quality Flagging
**Precondition:** `silver_health_checkup_clean` has been populated
**Steps:**
1. Query rows where systolic >250 or <60
**Expected Result:** These rows are flagged with `data_quality_flag = 'SUSPECT'`
**Actual Result:** _[To be filled Day 17]_
**Status:** _[Pending]_

## TC-04: Company SCD2 History Tracking
**Precondition:** `companies_master_v2_scd_test.csv` (updated company data) has been loaded
**Steps:**
1. Run the SCD2 MERGE logic
2. Query `silver_company_dim_scd2` for a company known to have changed
**Expected Result:** Two rows exist for that company — one with `is_current=false` and a populated `effective_end`, one with `is_current=true`
**Actual Result:** _[To be filled Day 17]_
**Status:** _[Pending]_

## TC-05: Company-wise KPI Dashboard
**Precondition:** `gold.company_summary` table is populated
**Steps:**
1. Open Power BI Dashboard 1
2. Filter by a specific company using the slicer
**Expected Result:** KPI cards (Employees Scanned, Avg BMI, High BP Rate %) update correctly for the selected company
**Actual Result:** _[To be filled Day 17]_
**Status:** _[Pending]_

## TC-06: Camp Performance Dashboard
**Precondition:** `gold.camp_performance` table is populated
**Steps:**
1. Open Power BI Dashboard 2
2. Sort the table by Net Margin
**Expected Result:** Camps are correctly ranked worst-to-best by margin; KPI card total matches sum of table values
**Actual Result:** _[To be filled Day 17]_
**Status:** _[Pending]_

## TC-07: Device Maintenance Dashboard
**Precondition:** `gold.device_maintenance` table is populated
**Steps:**
1. Open Power BI Dashboard 3
2. Check devices flagged "Due Soon"
**Expected Result:** Devices with `days_until_due` below threshold show status "Due Soon" with correct conditional formatting
**Actual Result:** _[To be filled Day 17]_
**Status:** _[Pending]_

## TC-08: BP Flag Derivation
**Precondition:** `silver_health_checkup_clean` has systolic/diastolic values populated
**Steps:**
1. Query rows where systolic >140 or diastolic >90
**Expected Result:** These rows are flagged `bp_flag = 'High'`; all others correctly flagged Normal/Low
**Actual Result:** _[To be filled Day 17]_
**Status:** _[Pending]_