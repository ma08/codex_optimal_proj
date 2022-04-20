
import math

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        div = [int(x) for x in input().split()][1:]
        div.sort()
        ans = math.gcd(div[0], div[1])
        for d in range(2, n):
            ans = math.gcd(ans, div[d])
        if ans > 1:
            print(ans)
        else:
            print(-1)

if __name__ == '__main__':
    main()
