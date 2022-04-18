
N, S, R = map(int, input().split())
D = set(map(int, input().split()))  # damaged
B = set(map(int, input().split()))  # backup

c = 0  # count

for i in range(1, N+1):
    if i in D:
        if i-1 in B:
            B.remove(i-1)
        elif i+1 in B:
            B.remove(i+1)
        else:
            c += 1
print(c)
