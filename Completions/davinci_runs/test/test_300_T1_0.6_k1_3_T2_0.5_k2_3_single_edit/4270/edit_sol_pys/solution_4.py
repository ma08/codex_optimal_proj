N = int(input())
V = [int(x) for x in input().split()]
V.sort()
while len(V) > 1:
    a = V.pop(0)
    b = V.pop(0)
    V.append((a + b)/2)
    V.sort()
print(V[0])
