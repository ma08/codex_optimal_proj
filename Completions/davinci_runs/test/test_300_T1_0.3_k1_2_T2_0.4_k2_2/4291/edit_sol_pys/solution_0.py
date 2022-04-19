

n, m = map(int, input().split())
a = list(map(int, input().split()))

# create a list of the indices of where A occurs
a_indices = []
for i in range(n):
    if a[i] == 1:
        a_indices.append(i)

# for each query, find the number of As in the substring
for i in range(m):
    l, r = map(int, input().split()) - 1
    print(a_indices[r] - a_indices[l] + 1)
