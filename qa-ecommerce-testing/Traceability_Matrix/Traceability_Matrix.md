# QA Manual Testing Portfolio - Ecommerce application testing - Traceability Matrix 

## 🚀 Author
Bojan Brankovic

# Traceability Matrix

## 📌 Overview
This traceability matrix maps business requirements to corresponding test cases, ensuring full test coverage and validation of application functionality.

---

## 📊 Traceability Matrix Table

| Requirement ID | Requirement Description | Test Cases | Priority | Coverage | Status |
|---------------|------------------------|-----------|----------|----------|--------|
| REQ01 | User can add products to cart | TC01, TC02 | High | Full | Covered |
| REQ02 | User can search products | TC03 | Medium | Full | Covered |
| REQ03 | User can complete checkout process | TC04, TC05 | High | Full | Issues Found |
| REQ04 | System handles session timeout | TC06 | Medium | Partial | Issues Found |
| REQ05 | UI adapts to different screen sizes | TC07 | Low | Full | Covered |

---

## 📈 Coverage Summary

- **Total Requirements:** 5  
- **Fully Covered:** 4  
- **Partially Covered:** 1  
- **Not Covered:** 0  

---

## ⚠️ Observations

- Critical issues found in checkout functionality (duplicate order creation)  
- Session timeout functionality is not working as expected (security concern)  
- UI responsiveness is stable across tested scenarios  

---

## 🎯 Conclusion

The application has strong test coverage across core functionalities.  
However, critical and security-related issues must be resolved before release.

---
