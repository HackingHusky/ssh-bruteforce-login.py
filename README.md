# SSH Brute Force Login Script

A high-performance Python script designed to test the strength of SSH credentials by simulating dictionary-based brute force attacks. Utilizing the `paramiko` library, this tool automates authentication requests against an SSH server using a user-provided wordlist.

---

## Technical Features

*   Automated Authentication: Automates credential stuffing and brute force evaluation against the standard SSH protocol.
*   Robust Transport Layer: Built on top of the Paramiko library for secure and accurate cryptographic negotiation.
*   Clear Auditing Logs: Provides immediate terminal feedback identifying valid authentication pairs versus rejected attempts.

---

## Prerequisites

Before running the tool, ensure your system meets the following software requirements:

*   Python 3.x
*   Pip (Python Package Installer)

---

## Installation

Follow these operational steps to provision the codebase and configure dependencies on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd ssh-bruteforce-login.py
   ```

2. Install the required runtime libraries:
   ```bash
   pip install paramiko
   ```

---

## Usage

The script evaluates a single targeted service at a time and requires a formatted password dictionary file containing one entry per line.

### Syntax

```bash
python ssh_brute_force.py <target_ip> <username> <password_file>
```

### Argument Layout

*   `<target_ip>`: The IP address or fully qualified domain name (FQDN) of the destination SSH server.
*   `<username>`: The explicit system user profile identity you are validating (e.g., root, admin, ubuntu).
*   `<password_file>`: The absolute or relative local path pointing to your payload text file containing test passwords.

### Execution Example

```bash
python ssh_brute_force.py 192.168.1.1 root passwords.txt
```

---

## Disclaimer and Legal Notice

This application is strictly engineered for educational purposes, legitimate security audits, defensive validation routines, and authorized Capture The Flag (CTF) deployment. Conducting credential stuffing or brute force assessments against network resources without prior explicit, written authorization from the infrastructure owner is strictly illegal. 

The author assumes zero liability or accountability for secondary damages, misuse, or illegal activities carried out using this software framework.

---

## License

This software utility is distributed openly under the provisions of the permissive MIT License. Review the repository LICENSE asset file for exhaustive documentation regarding redistribution or code modification clauses.
