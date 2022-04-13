


import sys

def main():
    passwords = []
    for line in sys.stdin:
        passwords.append(line.strip().split(' '))
    passwords = sorted(passwords, key=lambda x: float(x[1]))
    # print(passwords)
    expected_attempts = 0
    for i, password in enumerate(passwords):
        # print(password)
        expected_attempts += (i+1)*float(password[1])
    print(expected_attempts)


if __name__ == "__main__":
    main()
