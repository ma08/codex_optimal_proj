
def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        print(2)
        return
    ans = 1
    ans_1 = 1
    ans_2 = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            ans_1 += 1
        else:
            ans_1 = 1
        ans = max(ans, ans_1)
    for i in range(1, n-1):
        if a[i-1] < a[i+1]:
            ans_2 += 1
        else:
            ans_2 = 1
        ans = max(ans, ans_2)
    print(ans)

if __name__ == '__main__':
    main()
