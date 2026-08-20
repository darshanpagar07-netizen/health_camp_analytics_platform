# Source-to-Target Mapping (STTM) — Health Camp Analytics Platform

| # | Source System | Source Table/File                | Source Field                               | Transformation Logic                    | Target Table                | Target Field                       | Data Type |
|---|---|---|---|---|---|---|---|
| 1 | Vendor A      |vendor_a_medcamp_uploads.csv      | EmpID                                      | Direct rename                           | silver_health_checkup_clean | employee_id                        | string |
| 2 | Vendor A      |vendor_a_medcamp_uploads.csv      | BP_Sys                                     | Cast to int, rename                     | silver_health_checkup_clean | bp_systolic                        | int |
| 3 | Vendor A      |vendor_a_medcamp_uploads.csv      | BP_Dia                                     | Cast to int, rename                     | silver_health_checkup_clean | bp_diastolic                       | int |
| 4 | Vendor B      |vendor_b_healthfirst_uploads.xlsx | Systolic                                   | Cast to int, rename                     | silver_health_checkup_clean | bp_systolic                        | int |
| 5 | Vendor B      |vendor_b_healthfirst_uploads.xlsx | Body_Mass_Index                            | Cast to double, rename                  | silver_health_checkup_clean | bmi                                | double |
| 6 | Vendor C      |vendor_c_careplus_uploads.csv     | test_value (where test_type='BP_Systolic') | Pivot long→wide, cast to int            | silver_health_checkup_clean | bp_systolic                        | int |
| 7 | Vendor C      |vendor_c_careplus_uploads.csv     | test_value (where test_type='BMI')         | Pivot long→wide, cast to double         | silver_health_checkup_clean | bmi                                | double |
| 8 | Bronze        |bronze_camp_master_raw            | company_name, location                     | Dedup on camp_id, SCD2 MERGE            | silver_company_dim_scd2     | company_name, location, is_current | string, string, boolean |
| 9 | Silver        |silver_health_checkup_clean       | bp_systolic, bp_diastolic                  | CASE WHEN thresholds (>140/>90 = High)  | silver_health_checkup_clean | bp_flag                            | string |
| 10 | Silver       |silver_health_checkup_clean       | bp_systolic                                | CASE WHEN (>250 or <60)                 | silver_health_checkup_clean | data_quality_flag                  | string |
| 11 | Bronze       |bronze_device_master_raw          | next_service_due                           | DATEDIFF from current_date              | gold_device_maintenance     | days_until_due, status             | int, string |
| 12 | Bronze       |bronze_finance_raw                | revenue, staff_cost, consumables_cost      | revenue − staff_cost − consumables_cost | gold_camp_performance       | net_margin                         | int |

*(12 rows — covers all 3 vendor formats, SCD2 dimension mapping, and derived-field logic across Bronze → Silver → Gold layers.)*