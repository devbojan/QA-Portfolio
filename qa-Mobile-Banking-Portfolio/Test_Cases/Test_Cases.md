#QA Manual Testing Portfolio - Mobile Bank QA Project - Test Cases

## 🚀 Author
Bojan Brankovic 

# Test Cases

| TestCaseID   | Title                      | Description                   | Preconditions        | ExpectedResult         | Priority   | Type     |
|:-------------|:---------------------------|:------------------------------|:---------------------|:-----------------------|:-----------|:---------|
| TC01         | View account balance       | User sees correct balance     | Open app             | Balance displayed      | High       | Positive |
| TC02         | View transaction history   | List of transactions shown    | Open history         | Transactions visible   | High       | Positive |
| TC03         | Internal transfer          | Transfer between own accounts | Valid accounts       | Success message        | High       | Positive |
| TC04         | External transfer          | Transfer to other bank        | Valid IBAN           | Success/confirmation   | High       | Positive |
| TC05         | Add new beneficiary        | Save recipient                | Valid details        | Saved successfully     | Medium     | Positive |
| TC06         | Bill payment               | Pay utility bill              | Valid biller         | Payment success        | High       | Positive |
| TC07         | Scheduled payment          | Set future payment            | Valid date           | Scheduled confirmation | Medium     | Positive |
| TC08         | Card freeze                | Freeze debit card             | Card active          | Card frozen            | High       | Positive |
| TC09         | Card unfreeze              | Unfreeze card                 | Card frozen          | Card active            | High       | Positive |
| TC10         | ATM withdrawal limit check | Check daily limit             | Login required       | Limit displayed        | Medium     | Positive |
| TC11         | Push notifications         | Receive transaction alerts    | Enable notifications | Alert received         | Medium     | Positive |
| TC12         | Login session timeout      | Auto logout after inactivity  | Idle session         | Logged out             | High       | Negative |
| TC13         | Change PIN                 | Update card PIN               | Valid old PIN        | PIN updated            | High       | Positive |
| TC14         | Currency conversion        | View FX rates                 | Open FX screen       | Rates displayed        | Low        | Positive |
| TC15         | Download statement         | Export PDF statement          | Select date range    | File downloaded        | Medium     | Positive |
| TC16         | Search transactions        | Filter transactions           | Enter keyword        | Filtered results       | Low        | Positive |
| TC17         | Add new device             | Device registration           | New device login     | Device added           | High       | Positive |
| TC18         | Biometric login            | Face/fingerprint login        | Enabled biometric    | Login success          | High       | Positive |
| TC19         | Logout                     | User logout                   | Click logout         | Session ended          | High       | Positive |
| TC20         | Support chat               | Contact support               | Open chat            | Chat available         | Low        | Positive |
