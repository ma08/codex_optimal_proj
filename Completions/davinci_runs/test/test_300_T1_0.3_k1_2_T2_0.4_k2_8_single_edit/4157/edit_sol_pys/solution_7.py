
n = int(input())
a = list(map(int, input().split()))

def check(n):
    if len(n) == 1:
        return n
    if len(n) == 2:
        if n[0] == n[1] // 2 or n[0] == n[1] * 3:
            return n
        else:
            return []
    if n[0] == n[1] // 2:
        return [n[0]] + check(n[1:])
    if n[0] == n[1] * 3:
        return [n[0]] + check(n[1:])
    return []

for i in range(n):
    if check(a[i:]) != []:
        print(*check(a[i:]))
        break
