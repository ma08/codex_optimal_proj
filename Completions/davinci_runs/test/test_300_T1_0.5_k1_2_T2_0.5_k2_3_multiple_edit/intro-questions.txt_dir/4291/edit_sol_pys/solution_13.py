

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                ans[i] += 1
    print(*ans)

if __name__ == '__main__':
    main()
