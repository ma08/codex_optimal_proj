import sys
sys.setrecursionlimit(10**7)

n, q = map(int, input().split())
s = input()

# create a list of the number of ACs in each substring
ac_counts = [0] * n
for i in range(1, n):
    if s[i-1] == 'A' and s[i] == 'C':
        ac_counts[i] = ac_counts[i-1] + 1
    else:
        ac_counts[i] = ac_counts[i-1]

# for each query, find the number of ACs in the substring
for i in range(q):
    l, r = map(int, input().split())
    print(ac_counts[r-1] - ac_counts[l-1])
