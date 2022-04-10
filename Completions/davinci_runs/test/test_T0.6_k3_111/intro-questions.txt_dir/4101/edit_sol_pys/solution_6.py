

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = [0] * n
    ans_1 = [0] * m
    for i in range(n):
        if a[i].count(1) % 2 == 1:
            ans[i] = 1
    for j in range(m):
        if [a[i][j] for i in range(n)].count(1) % 2 == 1:
            ans_1[j] = 1
    for i in range(n):
        for j in range(m):
            if a[i][j] != ans[i] ^ ans_1[j]:
                print('NO')
                return
    print('YES')
    print(''.join(map(str, ans)))
    print(''.join(map(str, ans_1)))

if __name__ == "__main__":
    main()
