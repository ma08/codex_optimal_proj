import math
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        div = [int(x) for x in input().split()]
        div.sort()
        ans = div[0]
        for d in div:
            ans = math.gcd(ans, d)
        if ans > 1:
            print(ans)
        else:
            print(-1)

if __name__ == '__main__':
    main()
