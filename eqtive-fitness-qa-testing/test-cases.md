# Test Cases – EQtive Fitness App

---

## TC-01: User Login

**Priority:** High  
**Severity:** Critical  

Steps:
1. Open app
2. Enter valid credentials
3. Tap Login

Expected:
User is logged in successfully

---

## TC-02: Start Workout Session

**Priority:** High  
**Severity:** Critical  

Steps:
1. Navigate to workout screen
2. Tap "Start"

Expected:
Workout session starts and timer begins

---

## TC-03: Stop Workout Session

**Priority:** High  
**Severity:** High  

Steps:
1. Start workout
2. Tap "Stop"

Expected:
Session ends and data is saved

---

## TC-04: Data Tracking Accuracy

**Priority:** High  
**Severity:** Critical  

Steps:
1. Start workout
2. Perform activity
3. End session

Expected:
Time, reps, and calories are recorded correctly

---

## TC-05: Background Behavior

**Priority:** High  
**Severity:** Critical  

Steps:
1. Start workout
2. Minimize app
3. Return after 2 minutes

Expected:
Session continues tracking correctly

---

## TC-06: Session History

**Priority:** Medium  
**Severity:** Medium  

Steps:
1. Complete workout
2. Open history

Expected:
Workout appears in history list

---

## TC-07: Invalid Input Handling

**Priority:** Medium  
**Severity:** Medium  

Steps:
1. Enter invalid data (if manual input exists)

Expected:
Validation message shown

---

## TC-08: App Performance

**Priority:** High  
**Severity:** High  

Steps:
1. Navigate between screens quickly

Expected:
No lag or crash
