

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        ans += min(a[i+1], b[i]-min(a[i], b[i])) if i < n-1 else 0
    print(ans)

if __name__ == '__main__':
    main()
