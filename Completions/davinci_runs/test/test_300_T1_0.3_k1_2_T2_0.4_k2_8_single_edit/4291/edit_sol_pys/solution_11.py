

n, q = map(int, input().split())
s = input()

# create a list of the indices of where AC occurs, and a list of the number of ACs in each substring
ac_indices = [0]
ac_count = [0]
for i in range(1, n):
    if s[i-1] == 'A' and s[i] == 'C':
        ac_indices.append(i)
        ac_count.append(ac_count[i-1] + 1)
    else:
        ac_indices.append(i)
        ac_count.append(ac_count[i-1])

# for each query, find the number of ACs in the substring by subtracting the count of ACs in the previous substring
for i in range(q):
    l, r = map(int, input().split())
    print(ac_count[r-1] - ac_count[l-1])
