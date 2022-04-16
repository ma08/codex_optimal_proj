

# SOLUTION

p, s = input().split()
i = 0
for c in p:
    i = s.find(c, i)
    if i == -1:
        print('FAIL')
        break
else:
    print('PASS')
