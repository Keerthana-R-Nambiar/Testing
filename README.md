# Vulnerable Demo Project 🚨

⚠️ This project is intentionally insecure and should only be used for:
- Security learning
- SAST testing
- Vulnerability demonstrations

## Vulnerabilities Included

### 1. SQL Injection (Python)
- User input is directly concatenated into SQL queries.
- Allows attackers to bypass authentication.

Example:
username=admin'--

---

### 2. Cryptographic Failures
- MD5 used for password hashing.
- Hardcoded secret key.
- No salting or key management.

---

### 3. Cross-Site Scripting (XSS)
- User input rendered directly into HTML.
- Allows script injection.

Example:
<script>alert('XSS')</script>

---

### 4. Broken Access Control
- Admin endpoints accessible without authentication.
- No role or permission checks.

---

### 5. Open Redirect
- User-controlled redirect URLs.
- Can be used for phishing attacks.

---

## ⚠️ Disclaimer
DO NOT deploy this project in production.
All vulnerabilities are intentional.
