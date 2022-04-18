S, T = input().split()
A, B = map(int, input().split())
U = input()
if S == U:
    print(str(A - 1) + " " + str(B))
else:
    print(str(A) + " " + str(B - 1))
