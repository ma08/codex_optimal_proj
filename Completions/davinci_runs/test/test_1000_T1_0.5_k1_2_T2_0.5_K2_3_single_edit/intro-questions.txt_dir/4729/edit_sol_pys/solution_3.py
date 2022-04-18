

def main():
    password = input("Enter password: ")
    message = input("Enter message: ")

    # Check if the password is valid
    password_validity = check_password_validity(password)
    if password_validity:
        print("PASS")
    else:
        print("FAIL")
        return

    # Check if the message is valid
    message_validity = check_message_validity(password, message)
    if not message_validity:
        print("FAIL")

def check_password_validity(password):
    # Check if the password is valid
    if len(password) < 3 or len(password) > 8:
        return False
    return True

def check_message_validity(password, message):
    # Check if the message is valid
    if len(message) < 10 or len(message) > 40 or len(password) > len(message):
        return False

    # Check if the message is valid for the password
    password_index = 0 # keep track of the index of the password
    for character in message:
        if character == password[password_index]: # check if the character is the same as the password char
            password_index += 1 # increment the index
            if password_index == len(password): # check if we are at the end of the password
                return True # return true if we are at the end of the password
    return False

main()
