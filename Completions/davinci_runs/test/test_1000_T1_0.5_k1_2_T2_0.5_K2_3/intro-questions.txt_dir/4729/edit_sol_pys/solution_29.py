

def main():
    password_string, message_string = input().split() # split the input into the password and the message
    password_index = 0
    for char in message_string: # iterate through the message
        if char == password_string[password_index]:
            password_index += 1
        if password_index == len(password_string):
            print('PASS') # if the password is complete, then print PASS
            return # end the program
    print('FAIL') # if the password is not complete, then print FAIL

if __name__ == "__main__":
    main()
