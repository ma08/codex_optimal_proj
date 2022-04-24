

import sys
n = int(sys.stdin.readline())

for i in range(n // 4 + 1):  # 切り捨て除算
    if (n - 4 * i) % 7 == 0:  # 剰余
        print("Yes")
        sys.exit()

print("No")
