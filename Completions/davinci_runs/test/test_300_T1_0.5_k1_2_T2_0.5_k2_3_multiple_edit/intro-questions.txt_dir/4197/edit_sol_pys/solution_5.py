from collections import deque



def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    b = list(map(int, input().split()))[::-1]
    a = deque(a)
    b = deque(b)
    ans = 0
    while k > 0:
        if a[-1] > b[-1]:
            ans += a[-1]
            a.pop()
        else:
            ans += b[-1]
            b.pop()
        k -= 1
    print(ans)


if __name__ == '__main__':
    main()
