import math

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        divs = [int(x) for x in input().split()]
        divs.sort()
        ans = divs[0]
        for d in divs:
            ans = math.gcd(ans, d)
        if ans > 1:
            print(ans)
        else:
            print(-1)

if __name__ == '__main__':
    main()
