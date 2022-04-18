

import fileinput

def main():
    for line in fileinput.input():
        line = line.strip()
        password, message = line.split()
        if is_valid_message(password, message):
            print("PASS")
        else:
            print("FAIL")

def is_valid_message(password, message):
    for letter in password:
        if letter not in message:
            return False
    for i in range(len(message)-1):
        if password.index(message[i])>password.index(message[i+1]):
            return False
    return True

if __name__ == "__main__":
    main()
