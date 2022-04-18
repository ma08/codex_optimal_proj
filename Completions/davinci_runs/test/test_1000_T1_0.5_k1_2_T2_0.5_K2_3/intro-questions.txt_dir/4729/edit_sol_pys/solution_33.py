

import sys

def main():
    pwd, msg = sys.stdin.readline().split()
    pwd_i = 0
    for i in range(len(msg)):
        if pwd_i < len(pwd) and msg[i] == pwd[pwd_i]:
            pwd_i += 1
    if pwd_i == len(pwd):
        print('pass')
    else:
        print('fail')


if __name__ == '__main__':
    main()
