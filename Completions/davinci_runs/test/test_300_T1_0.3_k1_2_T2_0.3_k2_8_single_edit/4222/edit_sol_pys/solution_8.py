

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] == a[j] or a[j] == a[k] or a[k] == a[i]:
                    continue
                if a[i] + a[j] > a[k] and a[j] + a[k] > a[i] and a[k] + a[i] > a[j]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
