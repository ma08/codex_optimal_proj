

def check_password(password, msg):
    passw = list(password)
    for i in range(len(passw)):
        if passw[i] not in msg:
            return "FAIL"
        msg = msg[msg.index(passw[i])+1:]
    return "PASS"    

if __name__ == "__main__":
    print(check_password(input(), input()))
