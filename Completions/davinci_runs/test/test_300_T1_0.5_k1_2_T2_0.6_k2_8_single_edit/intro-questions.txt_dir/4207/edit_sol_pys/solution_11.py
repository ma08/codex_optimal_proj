

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort(reverse=True)
    a.insert(0, 0)
    ans = sum(a[:2])
    for i in range(2, n + 1):
        ans += sum(a[:i])
    print(ans - a[0])

if __name__ == '__main__':
    main()
