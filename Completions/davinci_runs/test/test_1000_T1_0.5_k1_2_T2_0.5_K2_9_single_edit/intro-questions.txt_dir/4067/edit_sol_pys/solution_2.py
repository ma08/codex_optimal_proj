
n = int(input())
s = input()

a = [0,0,0]
for i in range(n):
    a[int(s[i])] += 1

if a[1] == a[2]:
    print(s)
else:
    a[1] -= (a[1] - a[2]) // 3
    a[2] += (a[1] - a[2]) // 3
    ans = ''
    for i in range(n):
        if a[0] > 0:
            ans += '0'
            a[0] -= 1
        elif a[1] > 0:
            ans += '1'
            a[1] -= 1
        elif a[2] > 0:
            ans += '2'
            a[2] -= 1
    print(ans)
