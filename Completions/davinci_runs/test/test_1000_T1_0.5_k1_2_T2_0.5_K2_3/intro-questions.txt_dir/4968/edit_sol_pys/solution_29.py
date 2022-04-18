







N, S, R = map(int, input().split())
D = list(map(int, input().split()))
B = list(map(int, input().split()))

D.sort()
B.sort()

for i in D:
    if i - 1 in B:
        B.remove(i - 1)
        S -= 1
    elif i + 1 in B:
        B.remove(i + 1)
        S -= 1
    elif i in B:
        B.remove(i)
        S -= 1
print(S)
