
#!/bin/python3

m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

sym_diff = M.symmetric_difference(N)

for i in sorted(sym_diff):
    print(i)
