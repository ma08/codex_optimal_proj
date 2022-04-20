

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    ans1 = ans2 = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            ans1 += 1
        else:
            ans1 = 1
        ans = max(ans, ans1)
        if a[i - 1] < a[i + 1]:
            ans2 += 1
        else:
            ans2 = 1
        ans = max(ans, ans2)
    print(ans)

if __name__ == '__main__':
    main()
