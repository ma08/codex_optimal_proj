

password = input()
message = input()

for i in range(len(password)):
    if message.find(password[i]) == -1:
        print("FAIL")
        break
    else:
        message = message[message.find(password[i])+1:]
else:
    print("PASS")
