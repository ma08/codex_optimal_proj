

def check_passcode(passcode, message):
    passcode = list(str(passcode))
    for i in range(len(passcode)):
        try:
            index = message.index(passcode[i])
        except ValueError:
            return "FAIL"
        message = message[index+1:]
    return "PASS"

print(check_passcode(input(), str(input())))
