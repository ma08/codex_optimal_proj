

def check_passcode(passcode, message):
    passcode = list(passcode)  # convert to list
    for i in range(len(passcode)):
        try:
            index = message.index(passcode[i])  # find the index of the passcode in the message
        except ValueError:
            return "FAIL"
        message = message[index+1:]  # remove the found passcode from the message
    return "PASS"

print(check_passcode(input(), input()))
