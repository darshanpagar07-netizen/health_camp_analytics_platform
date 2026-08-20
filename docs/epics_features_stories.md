# Epics, Features & User Stories — Health Camp Analytics Platform

## EPIC 1: Standardized Multi-Vendor Data Ingestion (maps to BR-001)

### Feature 1.1: Bronze Layer Ingestion
**User Story 1.1.1:**
As a Data Engineer,
I want raw vendor files landed with source/ingestion-timestamp metadata,
So that I can trace any downstream number back to its original file.

**Acceptance Criteria (Given/When/Then):**
- Given a new vendor file is uploaded to the Volume,
- When the Bronze notebook runs,
- Then the file is appended (never overwritten) to its Bronze table with
  ingestion_ts populated.

### Feature 1.2: Vendor Format Standardization
**User Story 1.2.1:**
As a Business Analyst,
I want all 3 vendors' health data mapped to one common schema,
So that company-wise reports aren't split by vendor naming inconsistency.

**Acceptance Criteria:**
- Given Bronze tables for Vendor A, B, and C,
- When the Silver standardization job runs,
- Then a single silver_health_checkup_clean table exists with consistent column
  names (employee_id, camp_id, bp_systolic, bp_diastolic, sugar_fasting, bmi).

## EPIC 2: Data Quality & Governance (maps to BR-002, BR-006)

### Feature 2.1: Suspect Reading Detection
**User Story 2.1.1:**
As a Clinical Lead,
I want readings outside plausible medical ranges flagged automatically,
So that I don't act on obviously erroneous data.

**Acceptance Criteria:**
- Given a bp_systolic value > 250 or < 60,
- When Silver cleaning runs,
- Then data_quality_flag = 'SUSPECT' is set on that record.

### Feature 2.2: Company Dimension History (SCD2)
**User Story 2.2.1:**
As a Finance Lead,
I want historical company attribute changes preserved,
So that past reports don't silently change when a company's details are updated.

**Acceptance Criteria:**
- Given a company's location changes,
- When the SCD2 MERGE runs,
- Then the old row is marked is_current=false with an effective_end timestamp,
  and a new is_current=true row is inserted.

## EPIC 3: Business Reporting & Dashboards (maps to BR-003, BR-004, BR-005, BR-007)

### Feature 3.1: Company-wise KPI Dashboard
**User Story 3.1.1:**
As a Marketing Lead,
I want to see avg BMI and high-BP rate by company,
So that I can identify companies to prioritize for wellness-program renewal
pitches.

### Feature 3.2: Camp Performance Dashboard
**User Story 3.2.1:**
As an Operations Head,
I want to see revenue, cost, and net margin per camp,
So that I can identify loss-making camps early.

### Feature 3.3: Device Maintenance Dashboard
**User Story 3.3.1:**
As an Operations/Logistics Manager,
I want devices due for service within 7 days flagged in red,
So that I don't deploy faulty equipment to a live camp.