# QA Manual Testing Portfolio - Ecommerce application testing

## 🚀 Author
Bojan Brankovic

# Test Cases

| ID | Title | Module | Priority | Severity | Preconditions | Steps | Expected Result | Actual Result | Status |
|----|------|--------|----------|----------|--------------|-------|----------------|--------------|--------|
| TC01 | Add to Cart | Cart | High | Critical | User logged in, product available | Add product to cart | Product added | Works correctly | Pass |
| TC02 | Out of Stock | Cart | High | Major | Product stock = 0 | Try to add product | Error message | Error displayed | Pass |
| TC03 | Search Case | Search | Medium | Minor | User on homepage | Search laptop/LAPTOP | Same results | Works correctly | Pass |
| TC04 | Checkout Valid | Checkout | High | Critical | Product in cart | Complete checkout | Order success | Order placed | Pass |
| TC05 | Checkout Double Click | Checkout | High | Critical | Product in cart | Click confirm multiple times | One order | Multiple orders | Fail |
| TC06 | Session Timeout | Security | Medium | Major | User logged in | Wait 30 minutes | Logout | Session active | Fail |
| TC07 | UI Responsive | UI | Low | Minor | App open | Resize screen | UI adapts | Works fine | Pass |
