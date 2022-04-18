# import sys
#
# def main():
#     a, b, c = map(int, sys.stdin.readline().split()) # a, b, c는 int형
#     if c % a == 0: # c가 a로 나누어 떨어지면
#         print("YES")
#     else: # 아니면
#         print("NO")
#
# if __name__ == "__main__":
#     main()

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if c % a == 0:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
