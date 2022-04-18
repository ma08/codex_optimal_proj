import sys

N = int(input())

for i in range(100, N + 1):
    if len(set(list(str(i)))) == 1: # set로 바꾸면 중복 제거가 가능하다.
        print(i)
        break
