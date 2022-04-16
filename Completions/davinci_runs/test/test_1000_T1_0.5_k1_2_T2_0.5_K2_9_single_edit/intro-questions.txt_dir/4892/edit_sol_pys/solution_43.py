

import sys

def main():
    passwords = []
    for line in sys.stdin:
        passwords.append(line.strip().split(' '))
    passwords.sort(key=lambda x: float(x[1]), reverse=True)
    # print(passwords)
    expected_attempts = 0.0
    for i, password in enumerate(passwords):
        # print(password)
        expected_attempts += (i+1.0)*float(password[1])
    print(expected_attempts)

if __name__ == "__main__":
    main()
