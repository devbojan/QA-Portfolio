# Test Plan – Café-Restaurant Management System

## 1. Objective
To validate the functionality, data integrity, and reliability of the Café-Restaurant Management System, focusing on order processing, billing, and role-based access control.

## 2. Scope

### In Scope
- User authentication & role-based access (Admin, Staff, Manager)
- Order creation and management
- Billing and payment calculations
- CRUD operations (menu, orders, users)
- Database consistency

### Out of Scope
- External integrations (payment gateways, if not implemented)
- Network-related performance

## 3. Test Types
- Functional Testing
- Integration Testing
- Regression Testing
- Data Validation Testing
- Exploratory Testing

## 4. Test Environment
- Windows OS
- .NET runtime
- SQL Server database
- Local deployment

## 5. Entry Criteria
- Application builds successfully
- Database is configured and accessible

## 6. Exit Criteria
- All critical flows tested
- No high severity defects open

## 7. Risks
- Incorrect billing calculations
- Data inconsistency in database
- Unauthorized access due to role misconfiguration
