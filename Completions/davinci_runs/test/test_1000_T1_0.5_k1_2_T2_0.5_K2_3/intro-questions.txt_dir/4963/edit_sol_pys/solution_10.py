from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c_a = Counter(a)
c_b = Counter(b)

c_a_keys = list(c_a.keys())
c_b_keys = list(c_b.keys())

if len(c_a_keys) < len(c_b_keys):
    for i in range(len(c_a_keys)):
        if c_a_keys[i] in c_b_keys:
            c_b[c_a_keys[i]] -= c_a[c_a_keys[i]]
            c_a[c_a_keys[i]] = 0
        else:
            print('NO')
            exit()
    for i in range(len(c_b_keys)):
        if c_b[c_b_keys[i]] != 0:
            print('NO')
            exit()
    print('YES')
else:
    for i in range(len(c_b_keys)):
        if c_b_keys[i] in c_a_keys:
            c_a[c_b_keys[i]] -= c_b[c_b_keys[i]]
            c_b[c_b_keys[i]] = 0
        else:
            print('NO')
            exit()
    for i in range(len(c_a_keys)):
        if c_a[c_a_keys[i]] != 0:
            print('NO')
            exit()
    print('YES')
