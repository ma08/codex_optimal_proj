

import sys

def main():
    pw, msg = sys.stdin.readline().split()  # read the password and message
    pw_i = 0
    for i in msg:  # loop through the message
        if pw_i < len(pw) and i == pw[pw_i]:  # if the character matches the password at the current index
            pw_i += 1  # increase the index of the password
    if pw_i == len(pw):  # if the index of the password is at the end, the password was found
        print('PASS')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
