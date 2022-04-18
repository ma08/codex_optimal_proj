
import fileinput


def main():  # main function
    for line in fileinput.input():
        line = line.strip()
        password, message = line.split()
        if is_valid_message(password, message):  # call is_valid_message function
            print("PASS")
        else:
            print("FAIL")


def is_valid_message(password, message):  # function to determine if a message is valid
    for letter in password:
        if letter not in message:
            return False
    for i in range(len(password)-1):
        if message.index(password[i])>message.index(password[i+1]):
            return False
    return True


if __name__ == "__main__":
    main()
