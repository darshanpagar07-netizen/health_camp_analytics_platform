# Business Requirements Document — Health Camp Analytics Platform

## 1. Document Control
Version: 1.0 | Author: Darshan Pagar | Date: 20-08-2026 | Status: Draft

## 2. Business Objective
Consolidate fragmented, vendor-specific health-checkup data into a governed reporting
layer that gives Operations, Marketing, Finance, and Clinical stakeholders real-time,
trustworthy KPIs — replacing manual multi-day Excel consolidation.

## 3. Scope
**In scope:** Camp master, 3 vendor health-checkup feeds, device maintenance, finance
data, Power BI reporting layer.
**Out of scope:** Real-time streaming ingestion, mobile app, patient-level PII exposure
to marketing.

## 4. Stakeholders & RACI
| Stakeholder | Role | R/A/C/I |
|---|---|---|
| Camp Operations Head | Business Owner | A |
| Marketing/Client Relations Lead | Consumer of company-wise reports | C |
| Finance Lead | Consumer of margin/revenue reports | C |
| Clinical Lead | Consumer of health-trend reports | C |
| Data/BI Team (Darshan) | Delivery | R |

## 5. Business Requirements
- **BR-001**: System shall consolidate health-checkup data from 3 vendors into one
  standardized schema.
- **BR-002**: System shall flag suspect/out-of-range health readings for data quality
  review.
- **BR-003**: System shall track company-wise health KPIs (avg BMI, high-BP rate) for
  renewal pitches.
- **BR-004**: System shall report camp-level revenue, cost, and net margin.
- **BR-005**: System shall flag devices due for maintenance within 7 days.
- **BR-006**: System shall maintain historical tracking of company/camp attribute
  changes (SCD Type 2).
- **BR-007**: System shall reduce manual reporting turnaround from days to real-time
  dashboard access.

## 6. Assumptions & Constraints
Synthetic data used in place of real vendor data (confidentiality). Databricks Free
Edition used in place of production Azure Databricks (cost constraint) — see
design_decisions.md.

## 7. Success Criteria / KPIs
- Reporting turnaround reduced by 40%+ (matches real production metric)
- 100% of health readings classified as OK/SUSPECT (no unclassified records)
- 0 devices overdue for maintenance without a dashboard flag

## 8. Sign-off
Business Owner: Darshan Pagar   Date: 20-08-2026