#QA Manual Testing Portfolio - Mobile Bank QA Project - Test Execution Report


## 🚀 Author
Bojan Brankovic 

# Test Execution Report

| TestCaseID   | Title               | Description                      | Steps                                      | Preconditions              | ExpectedResult              | ActualResult             | RequirementID   | Severity   | Status   |
|:-------------|:--------------------|:---------------------------------|:-------------------------------------------|:---------------------------|:----------------------------|:-------------------------|:----------------|:-----------|:---------|
| TC01         | View balance        | Check account balance visibility | Open app > login > go to dashboard         | User logged in             | Balance displayed correctly | Balance matches backend  | REQ_01          | High       | Pass     |
| TC02         | Transaction history | Verify transactions list         | Open app > login > transactions tab        | User logged in             | List displayed              | List displayed correctly | REQ_02          | High       | Pass     |
| TC03         | Internal transfer   | Transfer between own accounts    | Accounts selected > enter amount > confirm | Valid accounts             | Transfer success            | Success confirmed        | REQ_03          | High       | Pass     |
| TC04         | External transfer   | Transfer to external IBAN        | Enter IBAN > amount > confirm              | Valid IBAN                 | Transfer successful         | Success                  | REQ_04          | High       | Pass     |
| TC05         | Add beneficiary     | Save new recipient               | Open beneficiaries > add new               | Valid details              | Saved                       | Saved successfully       | REQ_05          | Medium     | Pass     |
| TC06         | Bill payment        | Pay utility bill                 | Bills > select provider > pay              | Valid biller               | Payment success             | Payment success          | REQ_06          | High       | Pass     |
| TC07         | Scheduled payment   | Schedule future payment          | Payments > schedule                        | Valid date                 | Scheduled                   | Scheduled confirmed      | REQ_07          | Medium     | Pass     |
| TC08         | Card freeze         | Freeze card                      | Cards > select card > freeze               | Active card                | Frozen                      | Frozen                   | REQ_08          | High       | Pass     |
| TC09         | Card unfreeze       | Unfreeze card                    | Cards > unfreeze                           | Frozen card                | Active                      | Active                   | REQ_09          | High       | Pass     |
| TC10         | ATM limit           | Check ATM limit                  | Profile > limits                           | Logged in                  | Limit shown                 | Limit shown              | REQ_10          | Medium     | Pass     |
| TC11         | Notifications       | Push alerts                      | Enable notifications > trigger transaction | Notifications enabled      | Alert received              | Delayed alert            | REQ_11          | Medium     | Fail     |
| TC12         | Session timeout     | Auto logout                      | Idle app                                   | Logged in                  | Auto logout                 | Auto logout              | REQ_12          | High       | Pass     |
| TC13         | Change PIN          | Update PIN                       | Settings > change PIN                      | Valid old PIN              | Updated                     | Updated                  | REQ_13          | High       | Pass     |
| TC14         | FX rates            | View exchange rates              | Open FX screen                             | Logged in                  | Rates displayed             | Rates displayed          | REQ_14          | Low        | Pass     |
| TC15         | Download statement  | Export PDF                       | Statements > download                      | Date range selected        | Downloaded                  | Downloaded               | REQ_15          | Medium     | Pass     |
| TC16         | Search transactions | Filter results                   | Search keyword                             | Transactions exist         | Filtered                    | Filtered                 | REQ_16          | Low        | Pass     |
| TC17         | Add device          | Register device                  | Login new device                           | New device                 | Added                       | Added                    | REQ_17          | High       | Pass     |
| TC18         | Biometric login     | Face/Fingerprint login           | Enable biometrics                          | Device supports biometrics | Login success               | Login success            | REQ_18          | High       | Pass     |
| TC19         | Logout              | User logout                      | Click logout                               | Logged in                  | Logged out                  | Logged out               | REQ_19          | High       | Pass     |
| TC20         | Support chat        | Open support chat                | Help > chat                                | App open                   | Chat available              | Chat available           | REQ_20          | Low        | Pass     |
