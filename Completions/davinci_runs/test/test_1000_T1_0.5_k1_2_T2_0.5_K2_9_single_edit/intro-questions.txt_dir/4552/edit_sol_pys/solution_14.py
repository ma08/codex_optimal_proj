

S = input()
ans = 0

for i in range(len(S)):
    if i % 2 == 0 and S[i] == 'L':
        ans += 1
    elif i % 2 == 1 and S[i] == 'R':
        ans += 1
print(ans)
