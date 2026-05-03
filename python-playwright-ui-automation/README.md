# 🧪 Playwright UI Automation Framework (Python)

## 📌 Overview
UI test automation project built using Playwright and Python, following Page Object Model (POM) design pattern.

The project demonstrates real-world QA automation practices including test structuring, reusable components, and validation of user flows.

---

## ⚙️ Tech Stack
- Python
- Playwright
- Pytest

---

## 🧱 Project Structure

python-playwright-ui-automation/
│
├── pages/ # Page Object Model classes
├── tests/ # Test cases
├── screenshots/ # Test execution evidence
├── requirements.txt
├── README.md

---

## ✅ Test Coverage

- Login functionality (positive scenario)
- Login validation (negative scenario)
- UI state verification using assertions

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
playwright install
python -m pytest -v

📸 Test Evidence

Screenshots are automatically captured during test execution and stored in the screenshots/ directory.

🧠 Key Features
Page Object Model (POM) implementation
Reusable and maintainable test structure
Locator-based element handling
Automated UI validation
Ready for extension (fixtures, CI/CD, additional flows)

🚀 Future Improvements
Add pytest fixtures for cleaner setup
Implement parametrized tests
Integrate with CI/CD (GitHub Actions)
Expand test coverage (logout, session handling, UI flows)

