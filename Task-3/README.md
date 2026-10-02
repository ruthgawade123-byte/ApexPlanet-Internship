# Task 3: Web Application Security

## 1. Objective
Identify, exploit, and remediate standard OWASP Top 10 vulnerabilities in a controlled web application testing environment.


## 2. Tools & Environment
- **Attacker OS:** Kali Linux
- **Target Platform:** Damn Vulnerable Web Application (DVWA v2.5)
- **Web Server & Backend:** Apache/2.4.10, PHP 8.4, MariaDB/MySQL
- **Testing Tools:** Burp Suite Community Edition, Web Browser (Firefox)

---

## 3. Execution & Attack Scenarios

### Step 1: SQL Injection (SQLi)
Objective:Exploit input handling flaws in database queries to extract backend user records.

Payload Injected:
sql
  ' OR '1'='1

Observation: The backend authentication logic evaluated the statement to true, dumping database records including admin, Gordon, 1337, Pablo, and Bob.   

### Step 2: Reflected Cross-Site Scripting (Reflected XSS)Objective: Inject a client-side JavaScript snippet via unvalidated URL parameters that executes immediately in the browser. 

Payload Injected:
HTML<script>alert(1)</script>

Observation: The script parameter was reflected unencoded directly back into the DOM response, rendering an alert dialog box.  


### Step 3: Stored Cross-Site Scripting (Stored XSS)Objective: Persist an arbitrary JavaScript payload in the application's guestbook database to execute across user sessions.   

Payload Injected:
HTML<script>alert('stored XSS')</script>

Observation: The malicious script was stored permanently; every visit or refresh to the page automatically triggered the JavaScript popup showing stored XSS.   

### Step 4: Cross-Site Request Forgery (CSRF)

Objective: Trigger an unauthorized state change by forcing an authenticated session to execute password modification requests. 

Observation: The password change request lacked unique anti-CSRF token verification, allowing administrative credential modification through forged HTTP requests.  

### Step 5: Local File Inclusion (LFI)
Objective: Manipulate file path parameters to force the web server to expose local system files.   
Observation: Parameter traversal allowed direct reading of local system files and internal templates via unvalidated input vectors.

Step 6: HTTP Request Interception & Traffic Inspection (Burp Suite)
Objective: Intercept and inspect raw HTTP request headers, sessions, cookies, and POST parameters using a local web proxy.   
Observation: Intercepted sensitive submission payloads, cookies, and header directives passing between the client browser and the Apache backend.

### 4. Remediation & Hardening StrategiesPrepared Statements (SQLi Mitigation): 
1.Use parameterized database queries (PDO/prepared statements) to separate query logic from user-supplied input.   
2.Context-Aware Sanitization & CSP (XSS Mitigation): Implement strict output encoding (e.g., htmlspecialchars) and enforce a Content Security Policy (CSP) header to restrict untrusted inline script execution[cite: 9, 10].
3.Anti-CSRF Tokens (CSRF Mitigation): Generate unpredictable, cryptographically strong synchronizer tokens validated per session, and set SameSite=Strict or SameSite=Lax cookie flags.   
4.Input Validation (LFI Mitigation): Restrict file inclusion parameters by hardcoded whitelisting rather than dynamic string concatenation
