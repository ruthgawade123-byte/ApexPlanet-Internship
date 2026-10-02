# Task 2: Network Security & Scanning

## 1. Objective
Learn and execute reconnaissance methodologies, network scanning, packet-level traffic analysis, and host-based firewall defense mechanisms.


## 2. Tools & Environment
- **Operating System:** Kali Linux[cite: 16]
- **Target Systems:** Localhost (`127.0.0.1`), Remote/Domain targets (`example.com`)
- **Tools Used:** WHOIS, Nslookup, Nmap, Wireshark, vsftpd, hping3, iptables


## 3. Execution & Attack Scenarios

### Step 1: Passive Reconnaissance (WHOIS & DNS Lookups)
- **Objective:** Gather domain registration records, registrar details, nameservers, and IP mappings.
- **Commands:**
  ```bash
  nslookup example.com
  whois example.com
  ping -c 4 example.com
'''
 Observation: Successfully gathered domain registrar information (IANA), active name servers, and verified ICMP network reachability.   

 
 ### Step 2: Port & Service Scanning (Nmap)
 Objective: Identify active ports, detect listening services/versions, and fingerprint operating systems.   
 Commands:
bash 
TCP SYN Stealth Scan with Version & OS Detection
sudo nmap -sS -sV -O 127.0.0.1

# UDP Port Scan
sudo nmap -sU 127.0.0.1

Observation: Enumerated default network services across TCP and UDP interfaces to identify potential listening vectors.  


### Step 3: Cleartext Credential Sniffing (Wireshark & FTP)Objective: Capture unencrypted network traffic and extract plaintext credentials.   
Commands:
Bash
Start vsftpd service
sudo systemctl start vsftpd

# Connect to the FTP server
ftp 127.0.0.1
Wireshark Display Filter:Plaintextftp

Observation: Because FTP transmits data unencrypted, packet capture analysis directly exposed the credentials (USER ftp-test and PASS kali).   

### Step 4: DoS Attack Simulation (SYN Flood with hping3)Objective: Simulate a Denial of Service (SYN flood) and examine network traffic signatures.   
Commands:
Bash
sudo hping3 -S -p 80 --flood 127.0.0.1
Wireshark Display Filter:Plaintexttcp.flags.syn == 1 && tcp.flags.ack == 0

Observation: A continuous flood of TCP SYN packets was generated without completing the three-way handshake, consuming network queue resources.   

### Step 5: Firewall Implementation (iptables)Objective: Configure host-level packet filtering to detect and block unauthorized network scanning.  
Commands:
Bash
Check current rules
sudo iptables -L -n -v

# Block incoming traffic to a specific port
sudo iptables -A INPUT -p tcp --dport 8080 -j DROP

# Verify port filtering with Nmap
nmap -p 8080 127.0.0.1

Observation: The targeted port transitioned to the filtered state in the Nmap scan output, confirming that incoming packets were dropped.   


### 4. Remediation & Hardening StrategiesEnforce Secure Protocols: 
Replace legacy plaintext services (FTP, HTTP, Telnet) with encrypted equivalents (SFTP/SSH, HTTPS) to mitigate packet sniffing risks.SYN Flood Mitigation: Enable TCP SYN Cookies (net.ipv4.tcp_syncookies = 1) and apply rate limiting at the firewall level.Port Surface Reduction: Close unused or unneeded listening services and restrict critical management ports using strictly defined iptables or firewall whitelist rules.   
