import math

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    if a[-1] >= m:
        print(1)
        return

    days = 0
    for i in range(n):
        m -= a[i]
        days += 1
        if m <= a[-1]:
            print(days)
            return

    print(days + math.ceil(m / a[-1]))


if __name__ == "__main__":
    main()
