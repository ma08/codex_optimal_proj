

import sys

def main():
    pw, msg = sys.stdin.readline().split()  # pw와 msg를 입력받는다
    pw_i = 0
    for i in range(len(msg)):  # msg의 길이만큼 반복
        if pw_i < len(pw) and msg[i] == pw[pw_i]:  # pw_i가 pw의 길이보다 작고, msg[i]와 pw[pw_i]가 같을 때
            pw_i += 1
    if pw_i == len(pw):
        print('PASS')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
