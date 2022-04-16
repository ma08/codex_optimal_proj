

import sys

def main():
    passwords = []
    for line in sys.stdin:
        passwords.append(line.strip().split(' '))
    passwords = sorted(passwords, key=lambda x: float(x[1]), reverse=False)
    # print(passwords)
    expected_attempts = 0
    for i, password in enumerate(passwords):
        expected_attempts += (i+1)*float(password[0])
    print(expected_attempts)

if __name__ == "__main__":
    main()
