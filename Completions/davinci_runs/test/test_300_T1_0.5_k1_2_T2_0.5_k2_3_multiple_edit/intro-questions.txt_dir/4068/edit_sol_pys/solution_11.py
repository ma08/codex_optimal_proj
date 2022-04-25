

n, m = map(int, input().split())
broken = set(map(int, [input() for _ in range(n)]))

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    if i in broken:
        continue
    dp[i] = dp[i-1] + dp[i-2]



# 예외처리
def main():
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        print("숫자를 입력하세요")


if __name__ == "__main__":
    main()


# 입력값이 없으면 바로 종료
# 입력값이 있으면 바로 종료
import sys


def main():
    while True:
        try:
            a, b = map(int, input().split())
            print(a+b)
        except:
            sys.exit(0)


if __name__ == "__main__":
    main()
print(dp[n] % 1000000007)
