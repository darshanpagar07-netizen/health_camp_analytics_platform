"""
Synthetic dataset generator — Health-Checkup Analytics Platform (Portfolio Rebuild)
Mimics real C2P-style corporate health camp data across 3 vendor formats,
with intentional dirty data for Bronze->Silver cleaning practice.
"""
from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

fake = Faker('en_IN')
Faker.seed(42)
random.seed(42)
np.random.seed(42)

OUT = "data/raw"

CAMP_TYPES = ["General", "Diabetes Specialist", "Cardiac Specialist", "Eye Camp"]
LOCATIONS = ["Pune", "Mumbai", "Nashik", "Nagpur", "Aurangabad", "Thane", "Kolhapur"]
VENDORS = ["MedCamp Services", "HealthFirst Diagnostics", "CarePlus Camps"]
DEVICE_TYPES = ["BP Monitor", "X-Ray Machine", "ECG Machine", "Glucometer", "Weighing Scale", "Vision Chart Unit", "Audiometer"]

N_COMPANIES = 40
N_CAMPS = 150
N_DEVICES = 200

COMPANIES = [fake.company() for _ in range(N_COMPANIES)]

# ---------------------------------------------------------------------------
# 1. CAMP MASTER
# ---------------------------------------------------------------------------
def generate_camp_master(n_camps=N_CAMPS):
    camps = []
    start_date = datetime(2025, 1, 1)
    for i in range(n_camps):
        camp_date = start_date + timedelta(days=random.randint(0, 590))
        camps.append({
            "camp_id": f"CMP{1000+i}",
            "company_name": random.choice(COMPANIES),
            "camp_date": camp_date.strftime("%Y-%m-%d"),
            "location": random.choice(LOCATIONS),
            "camp_type": random.choice(CAMP_TYPES),
            "vendor": random.choice(VENDORS),
        })
    df = pd.DataFrame(camps)
    # duplicate a few camp_ids by accident (real-world SharePoint re-upload issue)
    dupes = df.sample(3, random_state=1)
    df = pd.concat([df, dupes], ignore_index=True)
    return df

camp_master = generate_camp_master()
camp_master.to_csv(f"{OUT}/camp_master.csv", index=False)

camps_by_vendor = {v: camp_master[camp_master.vendor == v].camp_id.unique().tolist() for v in VENDORS}

# ---------------------------------------------------------------------------
# 2. VENDOR A — MedCamp Services (clean-ish CSV)
# ---------------------------------------------------------------------------
def dirty_value(val, missing_rate=0.02):
    return np.nan if random.random() < missing_rate else val

def generate_vendor_a(camp_ids, min_n=15, max_n=35):
    rows = []
    fake.unique.clear()
    for cid in camp_ids:
        for _ in range(random.randint(min_n, max_n)):
            bp_sys = random.randint(100, 160)
            # inject a few out-of-range / suspect readings
            if random.random() < 0.015:
                bp_sys = random.choice([280, 40, 310])
            rows.append({
                "EmpID": fake.unique.bothify("EMP####"),
                "CampID": cid,
                "BP_Sys": dirty_value(bp_sys),
                "BP_Dia": dirty_value(random.randint(65, 100)),
                "Sugar_Fasting": dirty_value(random.randint(70, 200)),
                "BMI": dirty_value(round(random.uniform(18.0, 34.0), 1)),
            })
    df = pd.DataFrame(rows)
    # inject duplicate EmpID+CampID rows
    dupes = df.sample(frac=0.02, random_state=2)
    df = pd.concat([df, dupes], ignore_index=True)
    return df

vendor_a = generate_vendor_a(camps_by_vendor["MedCamp Services"])
vendor_a.to_csv(f"{OUT}/vendor_a_medcamp_uploads.csv", index=False)

# ---------------------------------------------------------------------------
# 3. VENDOR B — HealthFirst Diagnostics (Excel, different column names)
# ---------------------------------------------------------------------------
def generate_vendor_b(camp_ids, min_n=15, max_n=30):
    rows = []
    fake.unique.clear()
    for cid in camp_ids:
        camp_row = camp_master[camp_master.camp_id == cid].iloc[0]
        for _ in range(random.randint(min_n, max_n)):
            rows.append({
                "Employee_Code": fake.unique.bothify("EMP-#####"),
                "CampID": cid,
                "Date_Of_Camp": camp_row.camp_date,
                "Systolic": dirty_value(random.randint(95, 165)),
                "Diastolic": dirty_value(random.randint(60, 102)),
                "FastingGlucose": dirty_value(random.randint(65, 210)),
                "Body_Mass_Index": dirty_value(round(random.uniform(17.5, 35.0), 1)),
                "Vision_Score": dirty_value(random.choice(["6/6", "6/9", "6/12", "6/18", "6/24"])),
            })
    return pd.DataFrame(rows)

vendor_b = generate_vendor_b(camps_by_vendor["HealthFirst Diagnostics"])
vendor_b.to_excel(f"{OUT}/vendor_b_healthfirst_uploads.xlsx", index=False)

# ---------------------------------------------------------------------------
# 4. VENDOR C — CarePlus Camps (long/nested: one row per employee per test)
# ---------------------------------------------------------------------------
def generate_vendor_c(camp_ids, min_n=15, max_n=25):
    rows = []
    fake.unique.clear()
    test_types = ["BP_Systolic", "BP_Diastolic", "Sugar_Fasting", "BMI", "Hearing_Test"]
    for cid in camp_ids:
        for _ in range(random.randint(min_n, max_n)):
            emp_id = fake.unique.bothify("CP-EMP-####")
            for t in test_types:
                if t == "BP_Systolic":
                    val = random.randint(100, 158)
                elif t == "BP_Diastolic":
                    val = random.randint(64, 98)
                elif t == "Sugar_Fasting":
                    val = random.randint(72, 195)
                elif t == "BMI":
                    val = round(random.uniform(18.2, 33.5), 1)
                else:
                    val = random.choice(["Normal", "Mild Loss", "Refer"])
                rows.append({
                    "employee_id": emp_id,
                    "camp_id": cid,
                    "test_type": t,
                    "test_value": dirty_value(val, 0.015),
                })
    return pd.DataFrame(rows)

vendor_c = generate_vendor_c(camps_by_vendor["CarePlus Camps"])
vendor_c.to_csv(f"{OUT}/vendor_c_careplus_uploads.csv", index=False)

# ---------------------------------------------------------------------------
# 5. DEVICE MASTER + MAINTENANCE LOG
# ---------------------------------------------------------------------------
def generate_device_master(n=N_DEVICES):
    rows = []
    today = datetime(2026, 8, 18)
    for i in range(n):
        last_service = today - timedelta(days=random.randint(10, 400))
        next_due = last_service + timedelta(days=random.choice([90, 180, 365]))
        rows.append({
            "device_id": f"DEV{5000+i}",
            "device_type": random.choice(DEVICE_TYPES),
            "assigned_camp_id": random.choice(camp_master.camp_id.tolist()),
            "location": random.choice(LOCATIONS),
            "last_service_date": last_service.strftime("%Y-%m-%d"),
            "next_service_due": next_due.strftime("%Y-%m-%d"),
        })
    return pd.DataFrame(rows)

device_master = generate_device_master()
device_master.to_csv(f"{OUT}/device_master_maintenance.csv", index=False)

# ---------------------------------------------------------------------------
# 6. FINANCE DATA (one row per camp)
# ---------------------------------------------------------------------------
def generate_finance(camp_df):
    rows = []
    for cid in camp_df.camp_id.unique():
        scanned = random.randint(40, 400)
        revenue = scanned * random.randint(250, 600)
        staff_cost = random.randint(8000, 35000)
        consumables_cost = int(scanned * random.uniform(30, 90))
        rows.append({
            "camp_id": cid,
            "employees_scanned": scanned,
            "revenue": revenue,
            "staff_cost": staff_cost,
            "consumables_cost": consumables_cost,
        })
    return pd.DataFrame(rows)

finance = generate_finance(camp_master)
finance.to_csv(f"{OUT}/finance_data.csv", index=False)

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print("camp_master:", camp_master.shape)
print("vendor_a:", vendor_a.shape)
print("vendor_b:", vendor_b.shape)
print("vendor_c:", vendor_c.shape)
print("device_master:", device_master.shape)
print("finance:", finance.shape)
