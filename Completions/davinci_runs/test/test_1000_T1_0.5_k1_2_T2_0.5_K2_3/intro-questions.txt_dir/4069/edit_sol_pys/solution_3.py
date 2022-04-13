

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if all(i % 2 == 0 for i in a):
            a = [i // 2 for i in a]
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
