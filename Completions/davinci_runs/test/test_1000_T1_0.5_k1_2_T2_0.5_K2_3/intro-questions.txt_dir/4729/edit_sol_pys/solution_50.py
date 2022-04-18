
#this is a comment
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
    for i in range(len(password)-1):
        if message.find(password[i])>message.find(password[i+1]):
            return False
    return True

if __name__ == "__main__":
    main()
