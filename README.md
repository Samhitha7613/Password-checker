# Password Strength Checker with Breach Detection

A simple Python tool to check password strength **and** if the password has been exposed in known data breaches.

---

## Features

1. **Password Strength Assessment**
   - Checks length, uppercase, lowercase, numbers, and symbols.
   - Detects common passwords like `password`, `123456`, `qwerty`.
   - Provides actionable suggestions to improve password strength.

2. **Breach Check**
   - Uses [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3) to detect if the password has appeared in data breaches.
   - Warns the user if the password is compromised.

3. **User-Friendly CLI**
   - Enter a password and get instant feedback.
   - Score displayed with improvement suggestions.

---

## Tech Stack

- **Python 3**
- Libraries:
  - `requests` → for API calls
  - `re` → regex for password pattern checks
  - `hashlib` → to hash passwords for API query

---

## How It Works

1. **Strength Check**  
   Evaluates:
   - Length
   - Uppercase & lowercase letters
   - Digits
   - Symbols
   - Common password words

2. **Breach Detection**  
   - SHA-1 hash of the password is calculated.
   - The first 5 characters are sent to HaveIBeenPwned API.
   - Checks if the suffix appears in the API response.
   - Returns the number of times the password appeared in breaches.

3. **Suggestions & Feedback**  
   - Lists improvements for weak passwords.
   - Gives warnings if the password is found in breaches.

---

## Usage

```bash
python password_checker.py
```
### Example
```bash
Enter your password: mypassword123

--- Password Analysis ---
Strength score: 3/6
Suggestions to improve:
- Add at least one uppercase letter
- Add at least one special character (!@#$...)
⚠️ This password has appeared in 1000 data breaches! Consider changing it.
```

## Notes

- Running the API check requires internet access.
- If using an online compiler that blocks network requests, you can skip the breach check and test only the strength analysis.
- For enhanced UI, a GUI can be added using `tkinter`.

## Future Improvements

- Add a **GUI version** with `tkinter`.
- Auto-generate **strong passwords** based on suggestions.
- Visual password strength meter using `matplotlib`.

# 📌 **GitHub Repository**

[Phishing URL Detector – Samhitha7613](https://github.com/Samhitha7613/Password-checker.git)

----------

