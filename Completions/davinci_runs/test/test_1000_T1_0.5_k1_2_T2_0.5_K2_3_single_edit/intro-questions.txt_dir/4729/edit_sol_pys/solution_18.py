def main():
    pass_string, message_string = input().split() #split the input into two strings
    pass_index = 0
    for char in message_string:
        if char == pass_string[pass_index]: #if the char in the message string is equal to the password string
            pass_index += 1
        if pass_index == len(pass_string): #if the index of the password is equal to the length of the password
            print('PASS')
            return
    print('FAIL')

if __name__ == "__main__":
    main()
