

def main():
    n = int(input())
    xs = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += xs[i] * xs[j]
    print(ans)

if __name__ == '__main__':
    main()
