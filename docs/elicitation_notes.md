# Elicitation Notes — Requirements Gathering Session

Simulated interview notes, one exchange per stakeholder persona, capturing raw needs
before organizing them into formal requirements.

**Q (to Camp Operations Head): What's the first thing you check every Monday morning?**
A: Which camps ran at a loss last week, and whether any camp came in significantly
under our expected employee turnout.

**Q: What slows you down today?**
A: Every vendor sends me a different file format. By the time I've manually lined up
three vendors' numbers, half the week is gone.

**Q (to Marketing/Client Relations Lead): What do you need to walk into a renewal
meeting confident?**
A: Company-wise health trend data — average BMI, high-BP rate — so I can show the
client the value of the program, or flag a concern before they do.

**Q: What slows you down today?**
A: I can't tell which companies have declining health metrics until it's too late to
proactively intervene or adjust the pitch.

**Q (to Finance Lead): What's the hardest part of your monthly close process?**
A: Reconciling revenue and cost figures across three vendors that don't use the same
column names, same currency formatting, or even the same reporting cadence.

**Q: What would "done" look like for you?**
A: One consistent table — camp ID, revenue, cost, margin — regardless of which vendor
ran it.

**Q (to Clinical Lead): What worries you most about the current data?**
A: I don't know which readings to trust. A BP reading of 300 could be a genuine
emergency or a faulty sensor, and right now I can't distinguish the two without manually
digging into the raw file.

**Q: What would help you most?**
A: An automatic flag on any reading outside a plausible medical range, so I only
manually review the ones that actually need it.

**Q (to Logistics Manager): How do you currently track device maintenance?**
A: Honestly, mostly from memory and a shared spreadsheet that's often out of date.
We've had a BP monitor go into a camp overdue for calibration because nobody caught it.

**Q: What would prevent that from happening again?**
A: A simple flag — anything due for service within the next 7 days should show up
somewhere I actually look before a camp goes out.

## Raw needs extracted (unorganized — feeds into BRD)
- Standardize 3 vendor formats into one schema
- Flag suspect/out-of-range health readings automatically
- Company-wise health KPI reporting (avg BMI, high-BP rate)
- Camp-level revenue/cost/margin reporting, consistent across vendors
- Device maintenance due-date flagging (7-day lookahead)
- Historical tracking of company/camp attribute changes over time
- Reduce manual reporting turnaround from days to real-time