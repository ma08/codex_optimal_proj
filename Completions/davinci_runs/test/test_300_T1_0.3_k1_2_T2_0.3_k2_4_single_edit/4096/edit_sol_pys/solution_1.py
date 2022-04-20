
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))[:n]

    a.sort(reverse=True)
    if sum(a) < m:
        print(-1)
        return

    days = 0
    for i in range(n):
        if a[i] >= m:  # if the biggest number is bigger than m, we can finish the job in one day
            days += 1
            m = 0
            break
        else:  # if the biggest number is smaller than m, we have to do the job for one more day
            days += 1
            m -= a[i]

    if m > 0:
        days += 1

    print(days)

if __name__ == '__main__':
    main()
