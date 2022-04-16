

import sys

def main():
    k = int(sys.stdin.readline().strip()) # k = 입력값
    i = 1  # i = 자리수
    while True:
        if not (7 * (10 ** i) - 7) % k:  # 7의 배수를 찾는 과정
            print(i + 1)  # 자리수 + 1
            break
        i += 1

if __name__ == '__main__':
    main()
