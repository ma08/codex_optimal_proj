'''
    File name: pw.py
    Author: xdtianyu@gmail.com
    Date created: 2015-08-16 18:31:03
    Date last modified: 2015-08-16 18:31:03
    Python Version: 2.7.6
'''

import sys

def main():
    pw, msg = sys.stdin.readline().split()
    pw_i = 0
    for i in range(len(msg)):
        if pw_i < len(pw) and msg[i] == pw[pw_i]:
            pw_i += 1
    if pw_i == len(pw):
        print('PASS')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
