# https://atcoder.jp/contests/abc138/tasks/abc138_d

n, q = map(int, input().split())
s = input()

# create a list of the indices of where AC occurs,
# and a list of the children of each node
ac_indices = {}
children = [[] for i in range(n)]
for i in range(n):
    if s[i] == 'A':
        ac_indices[i] = 0
    else:
        children[int(s[i])-1].append(i)

# for each query, find the number of ACs in the subtree
for i in range(q):
    l, r = map(int, input().split())
    ac_indices[l-1] += 1
    if r < n:
        ac_indices[r] -= 1

# find the cumulative sum of the ac_indices
for i in range(1, n):
    ac_indices[i] += ac_indices[i-1]

# add the ac_indices to the children
for i in range(n):
    for j in children[i]:
        ac_indices[j] += ac_indices[i]

# print the ac_indices
for i in range(n):
    print(ac_indices[i], end=' ')
print()
