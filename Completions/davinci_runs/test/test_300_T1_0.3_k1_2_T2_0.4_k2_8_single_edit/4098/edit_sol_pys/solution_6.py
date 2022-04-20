

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    ans = 0
    for i in range(n):
        for j in range(i, n):
            if l[j] - l[i] <= 5:
                ans = max(ans, j - i + 1)
            else:
                break

    print(ans)

if __name__ == '__main__':
    main()
