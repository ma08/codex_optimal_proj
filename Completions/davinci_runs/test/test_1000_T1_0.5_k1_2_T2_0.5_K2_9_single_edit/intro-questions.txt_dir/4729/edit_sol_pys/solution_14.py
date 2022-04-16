

def main():
    password = input()
    message = input()

    # Check if the password is valid
    password_validity = check_password_validity(password)
    if not password_validity:
        print("FAIL")
        return

    # Check if the message is valid
    message_validity = check_message_validity(password, message)
    if message_validity:
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

    # Check if the message is valid for the password
    password_index = 0
    for character in message:
        if character == password[password_index]:
            password_index += 1
            if password_index == len(password):
                return True

    return False

main()
