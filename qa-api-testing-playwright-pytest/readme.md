# API Testing with Playwright + Pytest

## 📌 Overview

This project demonstrates API test automation using **Pytest** and **Playwright (Python)**.

It includes:

* Automated API tests
* Positive and negative scenarios
* HTML reporting
* Automatic screenshot capture on failure
* JSON response visualization for debugging

---

## 🧰 Tech Stack

* Python
* Pytest
* Playwright
* pytest-html

---

## 📁 Project Structure

```
qa-api-playwright/
│
├── tests/
│   ├── test_users.py
│   └── test_negative.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── screenshots/
```

---

## ▶️ How to Run

Install dependencies:

```
pip install -r requirements.txt
playwright install
```

Run tests:

```
pytest
```

---

## 📄 Test Report

After execution, an HTML report is generated:

```
report.html
```

Open it in your browser to view:

* Test results
* Logs
* Execution details

---

## ❌ Negative Testing Example

One test is intentionally designed to fail in order to demonstrate:

* Error handling
* Debugging process
* Screenshot capture

---

## 📸 Failure Screenshot

Below is an example of a captured screenshot when a test fails:

![Failure Screenshot](screenshots/html-report-screenshot.jpg)

This screenshot contains:

* API response
* JSON data
* Debug-friendly formatting

---

## 🧠 Key Features

* ✔ API testing using Playwright request context
* ✔ Pytest fixtures for clean setup
* ✔ Automatic screenshot on failure
* ✔ JSON response visualization
* ✔ HTML reporting

---

## 🎯 Purpose

This project is designed as a **portfolio example** to demonstrate:

* Practical QA automation skills
* Understanding of API testing
* Test structure and reporting

---

## 🚀 Future Improvements

* Add POST/PUT test cases
* Parameterized tests
* CI integration (GitHub Actions)
* Attach screenshots directly in HTML report

---

## 👨‍💻 Author
Bojan Brankovic
QA Automation Portfolio Project

