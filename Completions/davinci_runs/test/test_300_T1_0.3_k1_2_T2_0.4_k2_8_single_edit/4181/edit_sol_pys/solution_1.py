

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        a[i+1] = max(a[i+1]-(b[i]-min(a[i], b[i])), 0)
    print(ans)

if __name__ == '__main__':
    main()
