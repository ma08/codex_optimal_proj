def solve(n, a, b, s):
    ans = 0
    cur_b, cur_a = b, a
    for i in range(n):
        if s[i]:
            if cur_a:
                cur_a -= 1
            elif cur_b:
                cur_b -= 1
        else:
            if cur_b:
                cur_b -= 1
            elif cur_a:
                cur_a -= 1
        if cur_b or cur_a:
            ans += 1
        else:
            break
    return ans

n, b, a = map(int, input().split())
s = list(map(int, input().split()))
print(solve(n, b, a, s))
