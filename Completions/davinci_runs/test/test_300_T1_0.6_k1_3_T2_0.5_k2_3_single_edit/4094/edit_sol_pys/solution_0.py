
import sys

K = int(sys.stdin.readline())

count = 0

while True:
    if int(str(7) * count) % K == 0:  # int(str(7) * count) = 7을 count번 반복한다.
        print(count)
        break
    count += 1
