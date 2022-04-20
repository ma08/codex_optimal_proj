

# SOLUTION

n = int(input())
s = []
for i in range(n):
    s.append(input())
if n == 1:
    print('YES')
    print(s[0])
else:
    s = sorted(s, key = len)
    for i in range(n-1):
        if s[i] not in s[i+1]:
            print('NO')
            break
    else:
        print('YES')
        for i in s:
            print(i)