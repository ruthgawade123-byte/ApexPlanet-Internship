# Task 5 – Phishing Detection and Incident Response

## Overview

This task focuses on creating a basic phishing detection tool and
simulating an incident response process.

The project was completed in a controlled educational environment.
The detection tool analyzes URLs for common phishing indicators and
assigns a simple risk score.

## Objectives

- Develop a basic phishing URL detection tool.
- Identify common indicators of phishing URLs.
- Test the tool using different URL examples.
- Simulate a phishing security incident.
- Apply basic incident response procedures.
- Document the results and lessons learned.

## Tools and Technologies

- Kali Linux
- Python 3
- GitHub
- Oracle VirtualBox
- HTML
- Python HTTP Server

## Project Scope

The project is limited to educational phishing detection and incident
response simulation.

No real phishing campaign was conducted, no credentials were collected,
and no real users or systems were targeted.

---

## 1. Phishing Detection Tool

A Python-based phishing detection tool was created.

The program accepts a URL as user input and checks for several common
phishing indicators.

### Detection Indicators

The tool checks for:

- HTTP instead of HTTPS
- IP addresses used instead of domain names
- Suspicious keywords such as `login`, `verify`, `account`, and
  `password`
- URL shortening services such as `bit.ly` and `tinyurl.com`
- Excessive subdomains
- The presence of an `@` symbol

The tool assigns a risk score based on the indicators detected.

### Classification

The results are classified as:

- **LOW RISK** – Score below 2
- **SUSPICIOUS** – Score 2 or 3
- **HIGH RISK / POSSIBLE PHISHING** – Score 4 or above

---

## 2. Test Case 1 – High-Risk URL

### URL Tested

`http://192.168.1.10/login`

### Result

**Risk Score:** 4

**Classification:** HIGH RISK / POSSIBLE PHISHING

### Indicators Detected

- Uses HTTP instead of HTTPS
- Uses an IP address instead of a domain name
- Contains the suspicious keyword `login`

This test demonstrates how multiple indicators can increase the risk
score of a URL.

---

## 3. Test Case 2 – Low-Risk URL

### URL Tested

`https://example.com`

### Result

**Risk Score:** 0

**Classification:** LOW RISK

### Indicators Detected

No obvious phishing indicators were detected.

This test demonstrates that the tool does not automatically classify
every URL as phishing.

> A LOW RISK result does not guarantee that a website is completely safe.
> It only means that no obvious indicators checked by this basic tool
> were detected.

---

## 4. Test Case 3 – URL Shortener

### URL Tested

`http://bit.ly/verify-account`

### Result

**Risk Score:** 4

**Classification:** HIGH RISK / POSSIBLE PHISHING

### Indicators Detected

- Uses HTTP instead of HTTPS
- Contains the suspicious keywords `verify` and `account`
- Uses a URL shortening service

This test demonstrates detection of a shortened URL combined with
other suspicious characteristics.

---

## 5. Phishing Awareness Simulation

A local phishing-awareness webpage was created as part of the project.

The webpage demonstrates common phishing characteristics such as:

- Suspicious sender addresses
- Urgent or threatening language
- Requests for sensitive information
- Suspicious links
- Unexpected messages
- Pressure to act quickly

The webpage also provides guidance on how users should respond to
suspicious emails.

No passwords, credentials, or personal information were collected.

The webpage was hosted locally using Python's HTTP server.

---

## 6. Incident Response Simulation

A simulated phishing incident was created using the high-risk URL
detected by the tool.

### Identification

The phishing detection tool analyzed the URL and classified it as:

**HIGH RISK / POSSIBLE PHISHING**

The tool identified multiple suspicious indicators.

### Containment

The suspicious URL was not opened or visited.

No credentials or personal information were entered.

The URL was isolated within the controlled simulation.

### Eradication

The simulated phishing link was treated as unsafe and removed from
the simulated environment.

### Recovery

No system compromise occurred during the simulation.

The environment remained safe and operational.

### Lessons Learned

- Check URLs carefully before clicking.
- Be cautious of unexpected login or verification requests.
- Do not provide credentials through suspicious links.
- Verify requests through official channels.
- Report suspected phishing attempts.

---

## 7. Results

The phishing detection tool was successfully tested using three different
URL examples.

| Test Case | Risk Score | Classification |
|------------|------------|----------------|
| Suspicious IP-based login URL | 4 | HIGH RISK / POSSIBLE PHISHING |
| `https://example.com` | 0 | LOW RISK |
| Shortened verification URL | 4 | HIGH RISK / POSSIBLE PHISHING |

The project demonstrated how simple URL characteristics can be used to
identify potential phishing indicators.

---

## 8. Files

- `detector.py` – Python phishing detection program
- `test_results.txt` – Test case results
- `incident_log.txt` – Simulated incident record
- `response_status.txt` – Incident response status
- `Task-5-Evidence.pdf` – Screenshots and practical evidence

---

## 9. Conclusion

This project provided practical experience in identifying common
phishing indicators and responding to a simulated phishing incident.

The Python detection tool successfully analyzed different URL examples
and produced risk classifications based on predefined indicators.

The incident response simulation demonstrated the basic stages of
identification, containment, eradication, recovery, and lessons learned.

The project was completed in a controlled educational environment and
did not involve real phishing activity or collection of user credentials.

## Disclaimer

All activities in this project were performed for educational purposes
in a controlled environment. No real users, accounts, credentials, or
unauthorized systems were targeted.
