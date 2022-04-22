from collections import Counter

N = int(input())
S = input()

C = Counter(S)

ans = N - sum(C.values())

print(ans)
