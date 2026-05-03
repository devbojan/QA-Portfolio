# Test Cases – Occasion.ly

---

## TC-01: Create Reminder

**Priority:** High  
**Severity:** High  

Steps:
1. Open app
2. Click "Create Reminder"
3. Enter title and date/time
4. Save

Expected:
Reminder is created and visible in list

---

## TC-02: Notification Trigger

**Priority:** High  
**Severity:** Critical  

Steps:
1. Create reminder for next 1 minute
2. Lock device
3. Wait

Expected:
Push notification appears at scheduled time

---

## TC-03: Edit Reminder

**Priority:** Medium  
**Severity:** Medium  

Steps:
1. Create reminder
2. Edit date/time
3. Save

Expected:
Updated reminder is saved correctly

---

## TC-04: Delete Reminder

**Priority:** Medium  
**Severity:** Medium  

Steps:
1. Create reminder
2. Delete it

Expected:
Reminder is removed

---

## TC-05: Recurring Reminder

**Priority:** High  
**Severity:** High  

Steps:
1. Create recurring reminder (daily)
2. Wait next day

Expected:
Notification triggers again

---

## TC-06: Past Time Validation

**Priority:** High  
**Severity:** High  

Steps:
1. Try to create reminder in the past

Expected:
Validation error shown

---

## TC-07: App in Background

**Priority:** High  
**Severity:** Critical  

Steps:
1. Create reminder
2. Minimize app
3. Wait

Expected:
Notification still appears

---
