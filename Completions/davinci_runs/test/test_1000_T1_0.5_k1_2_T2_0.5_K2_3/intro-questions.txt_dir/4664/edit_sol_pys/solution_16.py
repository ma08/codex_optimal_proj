# Enter your code here. Read input from STDIN. Print output to STDOUT



m = int(input())

M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))


sym_diff = M.difference(N).union(N.difference(M)) #symmetric difference


for i in sorted(sym_diff):
    print(i)
