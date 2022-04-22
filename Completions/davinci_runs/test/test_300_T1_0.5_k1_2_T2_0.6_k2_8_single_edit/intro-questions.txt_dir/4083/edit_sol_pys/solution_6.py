

# import sys

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    ans = 0

    while a[0] > a[k-1]:
        a[0] //= 2
        a.sort(reverse=True)
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
