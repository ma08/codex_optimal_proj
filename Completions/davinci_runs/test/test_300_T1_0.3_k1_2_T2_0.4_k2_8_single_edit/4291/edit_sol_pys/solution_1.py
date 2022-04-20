

n, q = map(int, input().split())
s = input()

# create a list of the indices of where AC occurs,
# and a list of the number of ACs in each substring
ac_counts = [0] * n
ac_indices = []
for i in range(n-1):
    if s[i] == 'A' and s[i+1] == 'C':
        ac_counts[i] = 1
    if i > 0:
        ac_counts[i] += ac_counts[i-1]
        ac_indices.append(i)

# for each query, find the number of ACs in the substring
for i in range(q):
    l, r = map(int, input().split())
    print(ac_counts[r-1] - ac_counts[l-1])
