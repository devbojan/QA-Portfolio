# Bug Reports – Eye-Net Mobile

---

## BUG-01: Delayed Collision Alert

Severity: Critical  
Priority: High  

Steps:
1. Simulate proximity scenario

Expected:
Immediate alert

Actual:
Alert delayed by several seconds

---

## BUG-02: Missing Notification in Background

Severity: Critical  
Priority: High  

Steps:
1. Put app in background
2. Trigger alert

Expected:
Notification received

Actual:
No notification displayed

---

## BUG-03: GPS Inaccuracy

Severity: High  
Priority: High  

Steps:
1. Enable GPS

Expected:
Accurate positioning

Actual:
Location offset observed

---

## BUG-04: App Crash on Permission Denial

Severity: Critical  
Priority: High  

Steps:
1. Deny location permission

Expected:
Graceful handling

Actual:
App crashes

---

## BUG-05: App Stops Tracking in Background

Severity: High  
Priority: High  

Steps:
1. Minimize app
2. Move device

Expected:
Tracking continues

Actual:
Tracking stops
