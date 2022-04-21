'''
n = int(input())
s = input()
'''
n = int(input())
s = input()
#s = '120110'
#n = len(s)
a = [0,0,0]
for i in range(n):
    a[int(s[i])] += 1
#print(a)
if a[1] == a[2]:
    print(s)
else:
    k = a[1] - a[2]
    if k < 0:
        k = -k
    if k % 3 == 0:
        a[1] -= k // 3
        a[2] += k // 3
    else:
        k //= 2
        a[1] -= k // 3
        a[2] += k // 3
        k = 2 * k % 3
        a[1] -= k // 3
        a[2] += k // 3
    print(a)
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
