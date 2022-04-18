
import sys

def main():
    passwords = []  #list of passwords
    for line in sys.stdin:
        passwords.append(line.strip().split(' '))  #splits the passwords into a list
    passwords = sorted(passwords, key=lambda x: float(x[1]), reverse=True)  #sorts the passwords by their probability
    # print(passwords)
    expected_attempts = 0
    for i, password in enumerate(passwords):
        # print(password)
        expected_attempts += (i+1)*float(password[1])  #calculates the expected number of attempts
    print(expected_attempts)  #prints the expected number of attempts

if __name__ == "__main__":
    main()
