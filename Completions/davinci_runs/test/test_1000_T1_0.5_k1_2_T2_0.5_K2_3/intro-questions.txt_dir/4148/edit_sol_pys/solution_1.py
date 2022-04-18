import sys

n = int(sys.stdin.readline())  # 회전 횟수
s = sys.stdin.readline()  # 암호화할 문자열

for i in range(len(s)):  # 문자열의 길이만큼 반복
    if ord(s[i]) + n > ord('Z'):  # 만약 암호화한 문자가 Z보다 크면
        print(chr(ord(s[i]) + n - 26), end="")  # 26만큼 빼준다.
    else:  # 아니면
        print(chr(ord(s[i]) + n), end="")  # 그냥 회전
