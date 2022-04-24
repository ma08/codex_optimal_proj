import sys
K = int(sys.stdin.readline())
count = 0

while True:
    if int(str(7) * count) % K == 0:
        print(count)
        break
    count += 1
