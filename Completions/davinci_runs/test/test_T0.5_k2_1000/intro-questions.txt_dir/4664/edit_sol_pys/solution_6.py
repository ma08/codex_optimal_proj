
m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

sym_diff = M.difference(N).union(N.difference(M))  # union() returns the union of two sets

for i in sorted(sym_diff):
    print(i)
