# Bug Reports – Café-Restaurant Management System

---

## BUG-01: Incorrect Total Calculation

**Severity:** Critical  
**Priority:** High  

Steps:
1. Add multiple items
2. Complete order

Expected:
Correct total

Actual:
Total amount incorrect

---

## BUG-02: Unauthorized Access

**Severity:** Critical  
**Priority:** High  

Steps:
1. Login as Staff
2. Access Admin features

Expected:
Access denied

Actual:
Access granted

---

## BUG-03: Order Not Saved

**Severity:** High  
**Priority:** High  

Steps:
1. Create order
2. Confirm

Expected:
Order stored in database

Actual:
Order missing

---

## BUG-04: Duplicate Records

**Severity:** Medium  
**Priority:** Medium  

Steps:
1. Create order

Expected:
Single record

Actual:
Duplicate entries in database

---

## BUG-05: App Crash on Invalid Input

**Severity:** High  
**Priority:** High  

Steps:
1. Enter invalid data

Expected:
Validation error

Actual:
Application crashes
