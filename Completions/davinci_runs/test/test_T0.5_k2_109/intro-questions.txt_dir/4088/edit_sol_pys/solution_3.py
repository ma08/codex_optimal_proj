
for _ in range(int(input())):
    s = input()
    n = int(input())
    b = list(map(int, input().split()))
    b.insert(0, 0)
    ans = [0] * n
    for i in range(n):
        for j in range(1, n + 1):
            if b[j] == b[i] + j - i:
                ans[i] = j
                break
    for i in range(n):
        for ch in s:
            if ans[i] == 0:
                print(ch, end='')
            elif ans[i] > 0:
                ans[i] -= 1
    print()
