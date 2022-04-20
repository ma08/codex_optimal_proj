
import sys

K = int(sys.stdin.readline())

count = 0

while True:
    if int(str(7) * count) % K == 0:  # 곱해진 숫자가 K로 나누어 떨어지면 종료
        print(count)
        break
    count += 1
