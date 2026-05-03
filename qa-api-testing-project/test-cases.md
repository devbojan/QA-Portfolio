# Test Cases – Swagger Petstore API

## Scope
Validation of CRUD operations and error handling for Pet endpoints.

---

## TC-01: Create new pet

**Endpoint:** POST /pet  
**Description:** Verify that a new pet can be created successfully  

**Priority:** High  
**Severity:** High  

**Steps:**
1. Send POST request with valid body

**Test Data:**
{
  "id": 1111,
  "name": "TestPet",
  "status": "available"
}

**Expected Result:**
- Status code: 200
- Response contains correct pet data

**Actual Result:**
- Status code: 200
- Pet successfully created

**Status:** PASS

---

## TC-02: Retrieve pet by ID

**Endpoint:** GET /pet/{id}  
**Description:** Verify that created pet can be retrieved  

**Priority:** High  
**Severity:** Medium  

**Steps:**
1. Send GET request with existing pet ID

**Expected Result:**
- Status code: 200
- Response contains correct pet ID

**Actual Result:**
- Status code: 200
- Data returned correctly

**Status:** PASS

---

## TC-03: Update existing pet

**Endpoint:** PUT /pet  
**Description:** Verify that pet data can be updated  

**Priority:** High  
**Severity:** High  

**Steps:**
1. Send PUT request with updated pet data

**Test Data:**
{
  "id": 1111,
  "name": "TestPetUpdated",
  "status": "sold"
}

**Expected Result:**
- Status code: 200
- Pet data updated

**Actual Result:**
- Status code: 200
- Update successful

**Status:** PASS

---

## TC-04: Delete pet

**Endpoint:** DELETE /pet/{id}  
**Description:** Verify that pet can be deleted  

**Priority:** High  
**Severity:** Medium  

**Steps:**
1. Send DELETE request with pet ID

**Expected Result:**
- Status code: 200
- Pet removed

**Actual Result:**
- Status code: 200
- Pet deleted successfully

**Status:** PASS

---

## TC-05: Get deleted pet (negative)

**Endpoint:** GET /pet/{id}  
**Description:** Verify API response for non-existing pet  

**Priority:** High  
**Severity:** High  

**Steps:**
1. Send GET request for deleted pet ID

**Expected Result:**
- Status code: 404
- Error message returned

**Actual Result:**
- Status code: 404
- Error response received

**Status:** PASS
