
def main():
    password = input()
    message = input()

    # Check if the password is valid
    if not check_password_validity(password):
        print("FAIL")
        return

    # Check if the message is valid
    if check_message_validity(password, message):
        print("PASS")
    else:
        print("FAIL")

def check_password_validity(password):
    # Check if the password is valid
    if len(password) < 3 or len(password) > 8:
        return False
    return True

def check_message_validity(password, message):
    # Check if the message is valid
    if len(message) < 10 or len(message) > 40:
        return False

    # Check if the message is valid for the password (password is a substring of the message)
    password_index = 0
    for character in message:
        if character == password[password_index]:
            password_index += 1
            if password_index == len(password):
                return True
    return False

main()
