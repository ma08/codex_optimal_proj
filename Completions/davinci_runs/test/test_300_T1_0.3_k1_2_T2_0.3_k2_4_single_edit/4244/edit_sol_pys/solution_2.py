

def main():
    n = int(input())
    x = list(map(int, input().split()))[:n]
    x.sort()
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n // 2]) ** 2
    print(ans)

if __name__ == '__main__':
    main()
