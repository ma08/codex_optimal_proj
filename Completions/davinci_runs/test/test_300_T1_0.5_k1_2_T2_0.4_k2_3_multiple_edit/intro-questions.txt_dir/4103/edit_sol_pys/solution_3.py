import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808

def main():
    n = int(input())
    s = input()
    t = input()
    ans = INTMAX
    for i in range(n):
        cnt = 0
        for j in range(n):
            if s[j] != t[(i+j)%n]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == "__main__":
    main()
