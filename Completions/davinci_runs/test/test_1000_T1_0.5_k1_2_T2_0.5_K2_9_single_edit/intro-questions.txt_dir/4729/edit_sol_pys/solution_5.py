

password, message = input().split()  # Get input

for i in range(len(password)):  # Check if the password is in the message
    if message.find(password[i]) == -1:  # If the password is not in the message print "FAIL"
        print("FAIL")
        break
    else:
        message = message[message.find(password[i])+1:]
else:
    print("PASS")
