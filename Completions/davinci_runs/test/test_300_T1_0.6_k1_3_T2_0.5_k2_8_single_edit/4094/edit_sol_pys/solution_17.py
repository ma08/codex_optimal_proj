
import sys

K = int(sys.stdin.readline())

count = 0

while True:
    if int(str(7) * count) % K == 0:  # 7을 count번 곱한 값을 정수로 바꾼 후 K로 나누어 나머지가 0인 경우
        print(count)
        break
    count += 1
