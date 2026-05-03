# Swagger Petstore API Testing Project

## 📌 Overview
This project demonstrates manual API testing of a RESTful service based on OpenAPI specification.

The goal is to simulate real-world QA workflow including test planning, execution, and defect reporting.

---

## 🎯 Scope
- CRUD operations testing (Create, Read, Update, Delete)
- Response validation
- Error handling and negative testing

---

## 🧪 Test Coverage

### ✔ Positive Scenarios
- Create new pet
- Retrieve pet by ID
- Update pet data
- Delete pet

### ✔ Negative Scenarios
- Retrieve non-existing pet (404)
- Validation gaps during pet creation

---

## 🛠 Tools Used
- Postman (Web version)
- Swagger Petstore API

---

## 🧰 Tools Used
- Postman (Web)
- Swagger Petstore API

---

## 📦 Postman Collection

The API testing collection is included in the `/postman` folder.

You can import it into Postman to reproduce all test scenarios including CRUD operations and negative test cases.

### How to use:
1. Open Postman
2. Click "Import"
3. Select `SwaggerPetstore_collection.json` from `/postman` folder
4. Run requests from the collection


## 📂 Project Structure
qa-api-testing-project/
│
├── postman/
│ ├── collection.json
│ ├── environment.json
│
├── screenshots/
├── test-cases.md
├── test-plan.md
├── bug-reports.md
├── README.md

---

## 📊 Test Documentation

- Test Plan → `test-plan.md`
- Test Cases → `test-cases.md`
- Bug Reports → `bug-reports.md`

---

## 📸 Screenshots

### Create Pet
![Create](screenshots/post-create-pet-success.jpg)

### Update Pet
![Update](screenshots/put-update-pet.jpg)

### Delete Pet
![Delete](screenshots/delete-pet-success.jpg)

### Error Handling
![Error](screenshots/get-pet-not-found.jpg)

---

## 🧠 Key QA Skills Demonstrated
- API testing fundamentals
- Test case design
- Negative testing
- Bug reporting (Jira-style)
- Understanding of REST API workflows

---

## 🚀 Outcome
This project reflects a practical approach to API testing and demonstrates readiness for real-world QA tasks in an Agile environment.
