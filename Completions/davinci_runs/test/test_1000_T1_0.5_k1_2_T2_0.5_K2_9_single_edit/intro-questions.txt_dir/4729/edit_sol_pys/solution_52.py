

import sys

def main():
    pw, msg = sys.stdin.readline().split() # 공백을 기준으로 두개의 문자열로 나눈다.
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
