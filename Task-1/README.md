# Task 1: Foundations of Cybersecurity & Lab Setup

1. Objective
Establish foundational knowledge in cybersecurity, Linux environments, basic networking, and cryptography, while configuring a functional virtual penetration testing laboratory

2. Lab Environment & Verification
- Host System: Virtualized Kali Linux Rolling[cite: 5, 16]
- Kernel Version: 6.19.14-kali-amd64[cite: 16]
- Network Interface: eth0 (Host-Only / NAT configured)[cite: 5, 16]

### Environment Check & Tool Verification
Executed system checks confirming Kali installation, network IP assignment, Nmap version, and Wireshark version[cite: 16].


## 3. Practical Steps & Implementation

### Step 1: Linux CLI Navigation & Permissions
Practiced directory traversal, file creation, and verified permissions using `ls -la`


### Step 2: Target Setup (DVWA Installation)
Installed and unpacked Damn Vulnerable Web Application (DVWA) dependencies including PHP 8.4.


### Step 3: Network Diagnostics (Ping & Traceroute)
Tested outbound network routing and ICMP echo handling.



### Step 4: Cryptography & Encryption (OpenSSL)
Generated file hashes and performed symmetric encryption/decryption using OpenSSL AES-256-CBC:
```bash
# Encryption
openssl enc -aes-256-cbc -salt -in secret.txt -out secret.enc

# Decryption
openssl enc -d -aes-256-cbc -in secret.enc -out decrypted.txt
