n = int(input())
ans = 0


def is_sgs(x):
    if x % 10 == 7:
        return True
    else:
        return False

for i in range(1, n + 1):
    if i % 3 == 0:
        if is_sgs(i):
            ans += 1
    elif i % 5 == 0:
        if is_sgs(i):
            ans += 1
    elif i % 7 == 0:
        if is_sgs(i):
            ans += 1

print(ans)
