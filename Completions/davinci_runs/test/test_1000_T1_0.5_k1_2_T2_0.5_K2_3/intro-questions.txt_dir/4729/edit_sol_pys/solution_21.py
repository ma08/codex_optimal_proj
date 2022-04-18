

def check_password(password, message):  # check if the password is in the message 
    if(password in message): 
        return "PASS"
    else:
        return "FAIL"
        
print(check_password(input("Password: "), input("Message: ")))
