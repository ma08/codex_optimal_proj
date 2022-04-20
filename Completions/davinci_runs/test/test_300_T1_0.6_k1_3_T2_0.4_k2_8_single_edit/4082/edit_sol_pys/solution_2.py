

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        print(2)
        return
    ans = 1
    ans1 = [1] * n
    ans2 = [1] * n
    for i in range(1, n):
        if a[i] > a[i-1]:
            ans1[i] = ans1[i-1] + 1
        else:
            ans1[i] = 1
        ans = max(ans, ans1[i])
    for i in range(1, n-1):
        if a[i-1] < a[i+1]:
            ans2[i] = ans2[i-1] + 1
        else:
            ans2[i] = 1
        ans = max(ans, ans2[i])
    print(ans)

if __name__ == '__main__':
    main()
