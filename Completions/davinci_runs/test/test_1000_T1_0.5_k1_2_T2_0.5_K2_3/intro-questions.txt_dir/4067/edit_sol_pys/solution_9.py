

n = int(input())
s = input()
#n = int(input())
#s = '120110'
#n = 6

a = [0,0,0]
for i in range(n):
    a[int(s[i])] += 1

# print(a)

if a[1] == 0 or a[2] == 0:
    print(s)
    ans = ''
else:
    k = a[1] - a[2]
    r = k // 3
    if k % 3 != 0:
        r += 1
    # print(r)
    if a[1] > a[2]:
        a[1] -= r
        a[2] += r
        # print(a)
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
    else:
        a[1] += r
        a[2] -= r
        for i in range(n):
            if a[0] > 0:
                ans += '0'
                a[0] -= 1
            elif a[2] > 0:
                ans += '2'
                a[2] -= 1
            elif a[1] > 0:
                ans += '1'
                a[1] -= 1
    print(ans)
