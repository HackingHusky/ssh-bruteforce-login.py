SSH Brute Force Login Script
Description
This Python script demonstrates a brute force attack on an SSH service using the paramiko library. It attempts to login to a specified SSH server using a list of passwords and prints whether the login was successful or not. This script is intended for educational purposes only. Unauthorized access to systems is illegal and unethical. Always ensure you have permission to test any system.

Requirements
Python 3.x

paramiko library

Installation

Clone the repository
git clone https://github.com/HackingHusky/ssh-bruteforce-login.py
cd ssh-bruteforce-login

Install the rewuire4d libarary:
pip install paramiko

Usage
Create a file containing a list of passwords (one per line).

Run the script:


python ssh_brute_force.py <hostname> <username> <password_file>

<hostname>: The IP address or domain name of the SSH server.

<username>: The username to attempt to log in with.

<password_file>: The path to the file containing the list of passwords.

Example:


python ssh_brute_force.py 192.168.1.1 root passwords.txt

Notes
Ensure you have permission to test the target SSH service.

This script is for educational purposes only. Unauthorized access to systems is illegal and unethical.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
paramiko library documentation for providing SSH connectivity.
