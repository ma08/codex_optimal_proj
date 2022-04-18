import sys
input = sys.stdin.readline
 

def solve(n, k, s):
    s = list(s)
    while k > 0:
        changed = False
        for i in range(n-1):
            if s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i] # 入れ替え
                k -= 1
                changed = True
                break
        if not changed:
            break
    return "".join(s)

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
