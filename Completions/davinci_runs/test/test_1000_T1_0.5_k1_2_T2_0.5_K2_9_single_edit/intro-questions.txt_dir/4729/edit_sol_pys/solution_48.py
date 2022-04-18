

def check_password(password, message):
    for i in range(len(password)):
        try:
            index = message.index(password[i])
        except ValueError:
            return "FAIL"
        message = message[index+1:]
    return "PASS"

print(check_password(input(), input()))
