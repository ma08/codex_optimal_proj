N = int(input())
S = input()


max_diff = 0
for i in range(1, N-1):
    s1 = set(S[:i])
    s2 = set(S[i:])
    if len(s1 | s2) > max_diff:
        max_diff = len(s1 | s2)

print(N-max_diff)
