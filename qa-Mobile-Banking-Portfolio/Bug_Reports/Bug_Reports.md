#QA Manual Testing Portfolio - Mobile Bank QA Project - Bug Report


## 🚀 Author
Bojan Brankovic 

# Bug Report Examples

## BUG-001 – Push Notifications Delayed
- Severity: Major
- Priority: Medium
- Related TC: TC11 (I was able to reproduce the issue related to TC11, where push notifications were delayed after a transaction.

The other bugs below were identified through a combination of risk-based testing and exploratory testing, focusing on critical banking functionalities such as transfers, security, and user session management.)

Steps:
1. Enable push notifications  
2. Perform a transaction (e.g. transfer)  
3. Wait for notification  

Expected:  
Push notification received instantly after transaction  

Actual:  
Notification is delayed significantly  

---

## BUG-002 – Balance Not Updated After Transfer
- Severity: Critical
- Priority: High
- Related TC: TC03

Steps:
1. Perform internal transfer between accounts  
2. Navigate back to dashboard  

Expected:  
Updated balance shown immediately  

Actual:  
Old balance still displayed until manual refresh  

---

## BUG-003 – External Transfer Accepts Invalid IBAN Format
- Severity: Critical
- Priority: High
- Related TC: TC04

Steps:
1. Enter invalid IBAN format (e.g. random numbers)  
2. Enter amount and confirm  

Expected:  
Validation error displayed  

Actual:  
Transfer proceeds without IBAN validation  

---


