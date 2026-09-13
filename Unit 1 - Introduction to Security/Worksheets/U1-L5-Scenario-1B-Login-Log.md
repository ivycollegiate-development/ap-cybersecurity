AP Cybersecurity — Unit 1 · Period 4 (Tue, Sep 8)   Name: ______________   Date: ______________

# Scenario 1B — Login Log Analysis

A coworker forwarded you their account login history. Something feels off. Review the log below and answer the questions.

## Login Log Table

| Entry | Date | Time (CST) | Device | IP Address | Status |
|-------|------|------------|--------|------------|--------|
| 1 | Sep 5 | 08:12 | Classroom PC-12 | 10.42.5.18 | Success |
| 2 | Sep 5 | 11:45 | Student Chromebook | 10.42.8.33 | Success |
| 3 | Sep 5 | 15:02 | Classroom PC-12 | 10.42.5.18 | Success |
| 4 | Sep 6 | 02:34 | Unknown — Linux | **142.54.195.17** | Success |
| 5 | Sep 6 | 08:05 | Classroom PC-12 | 10.42.5.18 | Success |
| 6 | Sep 6 | 12:30 | Student Chromebook | 10.42.8.33 | Success |
| 7 | Sep 6 | **14:15** | Unknown — Windows | **142.54.195.17** | **Failed × 3, then Success** |
| 8 | Sep 7 | 08:10 | Classroom PC-12 | 10.42.5.18 | Success |

## Analysis Questions

1. What information does this log contain? List the fields.

   ______________________________________________________________________

2. Which entries are suspicious? Circle the entry numbers in the table above, then explain why.

   Entry ___: ________________________________________________________________

   Entry ___: ________________________________________________________________

3. What pattern connects entries 4 and 7?

   ______________________________________________________________________

4. Entry 7 shows "Failed × 3, then Success." What does that pattern suggest?

   ______________________________________________________________________

5. If this were your account, what would you do next? Name at least two actions.

   ______________________________________________________________________

   ______________________________________________________________________

## Key Takeaways

- A single login from an unfamiliar IP can be the first sign of compromise.
- Repeated failures followed by success = credential brute-force or password guessing.
- Legitimate users rarely log in at 2 AM from unknown devices.