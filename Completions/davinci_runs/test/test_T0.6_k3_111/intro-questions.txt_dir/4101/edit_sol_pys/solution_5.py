

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = [0] * n
    ans_ = [0] * n
    for i in range(n):
        if a[i].count(1) % 2 == 1:
            ans[i] = 1
    for i in range(n):
        if [a[i][j] for j in range(m)].count(1) % 2 == 1:
            ans_[i] = 1
    for i in range(n):
        for j in range(m):
            if a[i][j] != ans[i] ^ ans_[j]:
                print('NO')
                return
    print('YES')
    print(''.join(map(str, ans)))
    print(''.join(map(str, ans_)))

if __name__ == "__main__":
    main()
