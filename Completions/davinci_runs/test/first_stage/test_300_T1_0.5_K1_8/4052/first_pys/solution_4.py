

n = int(input())
s = input()
t = input()

s_map = {}
t_map = {}
for i in range(n):
    s_map[s[i]] = i
    t_map[t[i]] = i

for i in range(n):
    if s_map[t[i]] < i:
        print(-1)
        exit(0)

print(s_map[t[0]])
for i in range(1, n):
    print(s_map[t[i]], end=" ")
    s_map[t[i - 1]] = s_map[t[i]]