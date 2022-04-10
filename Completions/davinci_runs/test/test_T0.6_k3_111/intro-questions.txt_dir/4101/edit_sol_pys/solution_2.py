

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = [0] * m
    ans_ = [0] * n
    for i in range(n):
        if a[i].count(1) % 2 == 1:
            ans_[i] = 1
    for j in range(m):
        if [a[i][j] for i in range(n)].count(1) % 2 == 1:
            ans[j] = 1
    for i in range(n):
        for j in range(m):
            if a[i][j] != ans_[i] ^ ans[j]:
                print('NO')
                return
    print('YES')
    print(*ans_)
    print(*ans)

if __name__ == "__main__":
    main()
