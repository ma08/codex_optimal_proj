

# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input()) # number of elements in set M
M = set(map(int, input().split())) # elements of set M
n = int(input()) # number of elements in set N
N = set(map(int, input().split())) # elements of set N

sym_diff = M.difference(N).union(N.difference(M))

for i in sorted(sym_diff):
    print(i)
