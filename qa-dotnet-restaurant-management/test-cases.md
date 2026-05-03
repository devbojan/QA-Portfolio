# Test Cases – Café-Restaurant Management System

---

## TC-01: User Login (Valid Credentials)

**Priority:** High  
**Severity:** Critical  

Steps:
1. Launch application
2. Enter valid username/password
3. Click Login

Expected:
User is logged in and redirected based on role

---

## TC-02: User Login (Invalid Credentials)

**Priority:** High  
**Severity:** High  

Steps:
1. Enter invalid credentials

Expected:
Error message displayed

---

## TC-03: Role-Based Access Control

**Priority:** High  
**Severity:** Critical  

Steps:
1. Login as Staff
2. Try accessing Admin panel

Expected:
Access denied

---

## TC-04: Create Order

**Priority:** High  
**Severity:** Critical  

Steps:
1. Select menu items
2. Add to order
3. Confirm order

Expected:
Order is created successfully

---

## TC-05: Billing Calculation

**Priority:** High  
**Severity:** Critical  

Steps:
1. Create order with multiple items
2. Apply pricing

Expected:
Total amount calculated correctly

---

## TC-06: Update Menu Item

**Priority:** Medium  
**Severity:** Medium  

Steps:
1. Edit menu item
2. Save changes

Expected:
Changes reflected in database

---

## TC-07: Delete Order

**Priority:** Medium  
**Severity:** Medium  

Steps:
1. Select order
2. Delete

Expected:
Order removed successfully

---

## TC-08: Database Consistency

**Priority:** High  
**Severity:** Critical  

Steps:
1. Create order
2. Check database records

Expected:
Data stored correctly without duplication
