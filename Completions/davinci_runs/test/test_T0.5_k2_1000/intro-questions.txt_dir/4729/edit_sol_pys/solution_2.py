

import sys

def main():
    password, msg = sys.stdin.readline().split(',')
    password_i = 0
    for i in range(len(msg)):
        if password_i < len(password) and msg[i] == password[password_i]:
            password_i += 1
    if password_i == len(password):
        print('PASS')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
