
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    a.sort(reverse=True)
    if sum(a) < m:  # 가장 큰 수부터 정렬해서 더해나가다가 m보다 크면 종료
        print(-1)
        return

    days = 0
    for i in range(n):  # 가장 큰 수부터 정렬해서 더해나가다가 m보다 작으면 종료
        if a[i] >= m:
            days += 1
            m = 0
            break
        else:
            days += 1
            m -= a[i]

    if m > 0:
        days += 1

    print(days)

if __name__ == '__main__':
    main()
