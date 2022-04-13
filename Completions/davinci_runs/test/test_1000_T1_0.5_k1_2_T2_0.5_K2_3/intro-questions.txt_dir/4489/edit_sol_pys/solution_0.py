
'''
# My Answer
n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for j in range(m)]

s_count = {}
t_count = {}

for i in s:
    if i in s_count:
        s_count[i] += 1
    else:
        s_count[i] = 1

for j in t:
    if j in t_count:
        t_count[j] += 1
    else:
        t_count[j] = 1

s_count = sorted(s_count.items(), key = lambda x: x[1], reverse = True)
t_count = sorted(t_count.items(), key = lambda x: x[1], reverse = True)

#print(s_count)
#print(t_count)

if len(s_count) >= len(t_count):
    ans = 0
    for i in range(len(t_count)):
        ans += s_count[i][1] - t_count[i][1]
    print(ans)
else:
    ans = 0
    for i in range(len(s_count)):
        ans += s_count[i][1] - t_count[i][1]
    print(ans)

'''

# Other's Answer
'''
n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]

ans = 0
for i in set(s):
    ans += s.count(i) - t.count(i)
print(ans)
'''
