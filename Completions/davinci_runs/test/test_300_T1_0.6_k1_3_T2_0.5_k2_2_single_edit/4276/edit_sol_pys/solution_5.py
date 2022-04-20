
import math
import sys

def main():
    x = int(input())
    ans = 0
    for i in range(1, x + 1):
        if i == 1:
            ans += 1
            continue
        ans += i * (i - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()
