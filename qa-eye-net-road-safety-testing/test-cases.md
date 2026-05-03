# Test Cases – Eye-Net Mobile

---

## TC-01: App Launch

Priority: High  
Severity: Critical  

Steps:
1. Open app

Expected:
App launches without crash

---

## TC-02: Permissions Handling

Priority: High  
Severity: Critical  

Steps:
1. Deny location permission

Expected:
App shows proper message and handles gracefully

---

## TC-03: GPS Detection

Priority: High  
Severity: Critical  

Steps:
1. Enable GPS
2. Move device

Expected:
Accurate real-time location tracking

---

## TC-04: Collision Alert Trigger

Priority: High  
Severity: Critical  

Steps:
1. Simulate proximity between users/devices

Expected:
Collision alert triggered in real-time

---

## TC-05: Notification Delivery

Priority: High  
Severity: Critical  

Steps:
1. Trigger alert
2. App in background

Expected:
Push notification received instantly

---

## TC-06: Background Behavior

Priority: High  
Severity: High  

Steps:
1. Minimize app
2. Continue movement

Expected:
Tracking and alerts continue

---

## TC-07: Network Loss Handling

Priority: High  
Severity: High  

Steps:
1. Disable internet

Expected:
App handles gracefully or shows fallback

---

## TC-08: App Resume

Priority: Medium  
Severity: Medium  

Steps:
1. Minimize app
2. Reopen

Expected:
App resumes correctly without reset
