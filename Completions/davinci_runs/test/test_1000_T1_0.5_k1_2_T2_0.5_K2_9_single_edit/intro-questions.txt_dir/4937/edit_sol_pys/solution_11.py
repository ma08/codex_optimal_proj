
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    a.reverse()
    start = 0
    end = a[0]
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        sum_ = 0
        for i in a:
            if i > mid:
                sum_ += i - mid
        if sum_ >= m:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    print(ans)

if __name__ == '__main__':
    main()
