
import sys

K = int(sys.stdin.readline())

count = 0

while True:
    if int(str(7) * count) % K == 0:  # 7을 문자열로 변환하여 곱한 후 정수로 변환
        print(count)
        break
    count += 1
