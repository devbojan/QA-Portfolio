# Bug Reports – Swagger Petstore API

---

## BUG-01: Inconsistent response for non-existing pet ID

**ID:** BUG-01  
**Title:** API returns inconsistent error structure for non-existing pet  

**Priority:** High  
**Severity:** Medium  
**Type:** Functional  

**Environment:** Swagger Petstore API v2  

---

**Steps to Reproduce:**
1. Send GET request to /pet/999999999

---

**Expected Result:**
- Status code: 404 Not Found
- Response should follow consistent error format
- Clear error message (e.g. "Pet not found")

---

**Actual Result:**
- Status code: 404
- Response structure is inconsistent / unclear
- Error message not standardized

---

## BUG-02: API allows creating pet with minimal required data

**ID:** BUG-02  
**Title:** Missing validation for required fields in pet creation  

**Priority:** Medium  
**Severity:** Medium  
**Type:** Validation  

**Environment:** Swagger Petstore API v2  

---

**Steps to Reproduce:**
1. Send POST request to /pet with incomplete body:
{
  "id": 2222
}

---

**Expected Result:**
- Status code: 400 Bad Request
- Validation error message

---

**Actual Result:**
- Status code: 200
- Pet is created without required fields

---

**Impact:**
- Data inconsistency
- Invalid records in system

---

**Status:** Open

**Impact:**
- Makes error handling harder on frontend
- Can cause issues in client-side validation

---

**Status:** Open
