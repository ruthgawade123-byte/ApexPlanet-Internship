# Task 4 – Exploitation & System Security

## Overview

This task focused on penetration testing methodology, controlled exploitation,
password security, phishing awareness, malware analysis, and system hardening.

All testing was performed in an isolated virtual lab using Kali Linux and
Metasploitable2.

## Lab Environment

- Attacker: Kali Linux
- Target: Metasploitable2
- Virtualization: Oracle VirtualBox
- Network: Host-Only Network
- Kali IP: 192.168.56.101
- Metasploitable2 IP: 192.168.56.102

## 1. Penetration Testing Methodology

The following methodology was followed:

1. Reconnaissance
2. Scanning
3. Exploitation
4. Post-Exploitation
5. Reporting

### Network Scanning

Nmap was used to identify open ports and running services on the
Metasploitable2 machine.

Command:

    nmap -sV 192.168.56.102

The scan identified services including FTP, SSH, HTTP, SMB, MySQL,
PostgreSQL, VNC and other services.

## 2. Exploitation with Metasploit

The VSFTPD 2.3.4 backdoor vulnerability was tested in the controlled
Metasploitable2 environment.

Metasploit module:

    exploit/unix/ftp/vsftpd_234_backdoor

The target and local host were configured and the exploit was executed.

A Meterpreter session was successfully opened on the target.

### Post-Exploitation

The following command was used:

    sysinfo

The target was identified as:

- Ubuntu 8.04
- Linux 2.6.24
- i686 architecture

A shell was also opened to demonstrate post-exploitation access.

The `hashdump` command was attempted, but the required `priv` extension
was not supported by the Linux Meterpreter payload used in this lab.

## 3. Password Attacks

### Hydra

Hydra was tested against the SSH service using a small password list
created specifically for the lab.

The attempt reached the SSH service but could not proceed because the
legacy OpenSSH server and the current SSH client could not negotiate a
compatible MAC algorithm.

Therefore, no successful password was claimed from this test.

### John the Ripper

John the Ripper was demonstrated using a controlled MD5 test hash.

The hash for the word `password` was created and placed in a test file.

John successfully recovered the test password using a small wordlist.

This demonstrated the risk of using weak password hashes.

## 4. Phishing Awareness Simulation

A local phishing-awareness webpage was created for educational purposes.

The page demonstrated:

- Suspicious sender
- Urgent language
- Requests for sensitive information
- Suspicious links
- Common phishing red flags
- Recommended user actions

No credentials or personal information were collected.

The page was hosted locally using Python's HTTP server.

## 5. Malware Basics

A harmless training sample was created for analysis.

Static analysis was performed using:

    file sample.txt
    ls -l sample.txt
    sha256sum sample.txt

The file type, permissions, size and SHA-256 hash were examined.

A harmless execution/output demonstration was also performed to illustrate
the concept of dynamic analysis.

No real malware was executed.

## 6. System Hardening

The system firewall configuration was examined using iptables.

A targeted firewall rule was added to block outbound traffic from Kali
to the Metasploitable2 lab IP:

    sudo iptables -A OUTPUT -d 192.168.56.102 -j DROP

The rule was then verified using:

    sudo iptables -L OUTPUT -n -v

UFW was also checked, but it was not installed in the environment.

## Key Learning Outcomes

- Understanding the penetration testing workflow
- Performing service and version scanning
- Exploiting a known vulnerability in a controlled lab
- Understanding post-exploitation
- Understanding password attack techniques
- Identifying phishing indicators
- Understanding basic malware analysis
- Applying basic firewall-based hardening

## Disclaimer

All exploitation and security testing activities were performed only
against intentionally vulnerable systems in an isolated educational
laboratory. No unauthorized real-world systems were targeted.
