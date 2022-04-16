

def check_password(password, message, n):
    for i in range(n):
        if password[i] not in message:
            return "FAIL"
        index = message.index(password[i])
        message = message[index+1:]
    return "PASS\n"

n = int(input())
password = input()
message = input()
print(check_password(password, message, n))
