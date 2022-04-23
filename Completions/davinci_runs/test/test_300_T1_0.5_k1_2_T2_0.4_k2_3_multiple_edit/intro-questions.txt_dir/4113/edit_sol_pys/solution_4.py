import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n // 4 + 1):
    if (n - 4 * i) % 7 == 0:  # 4와 7의 배수인지 확인
        print("Yes")
        sys.exit()

print("No")
