# QA Manual Testing Portfolio - Ecommerce application testing - Bug Report Examples

## 🚀 Author
Bojan Brankovic

# Bug Report Examples

## BUG-001 – Product Not Added to Cart
- Severity: Critical
- Priority: High
- Related TC: TC01

Steps:
1. Login to application  
2. Open product page  
3. Click "Add to Cart"  

Expected:  
Product is added to cart successfully  

Actual:  
Product is not added, no confirmation message shown  

---

## BUG-002 – Out-of-Stock Product Can Be Added
- Severity: Major
- Priority: High
- Related TC: TC02

Steps:
1. Navigate to product with stock = 0  
2. Click "Add to Cart"  

Expected:  
Error message displayed (Out of stock)  

Actual:  
Product is added to cart despite zero stock  

---

## BUG-003 – Search is Case Sensitive
- Severity: Minor
- Priority: Medium
- Related TC: TC03

Steps:
1. Enter "laptop" in search bar  
2. Note results  
3. Enter "LAPTOP" in search bar  

Expected:  
Same results returned  

Actual:  
Different results displayed  

---

## BUG-004 – Checkout Fails with Valid Data
- Severity: Critical
- Priority: High
- Related TC: TC04

Steps:
1. Add product to cart  
2. Proceed to checkout  
3. Enter valid details  
4. Confirm order  

Expected:  
Order is successfully placed  

Actual:  
Checkout fails / no confirmation displayed  

---

## BUG-005 – Duplicate Orders Created on Multiple Click
- Severity: Critical
- Priority: High
- Related TC: TC05

Steps:
1. Add product to cart  
2. Proceed to checkout  
3. Click "Confirm Order" multiple times quickly  

Expected:  
Only one order is created  

Actual:  
Multiple orders are created  

---

## BUG-006 – Session Does Not Expire After Timeout
- Severity: Major
- Priority: Medium
- Related TC: TC06

Steps:
1. Login to application  
2. Stay inactive for 30+ minutes  

Expected:  
User session expires and user is logged out  

Actual:  
Session remains active  

---

## BUG-007 – UI Not Responsive on Resize
- Severity: Minor
- Priority: Low
- Related TC: TC07

Steps:
1. Open application  
2. Resize browser window / use mobile view  

Expected:  
UI adjusts to screen size properly  

Actual:  
UI elements overlap or break layout  
