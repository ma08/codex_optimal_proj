

n, q = map(int, input().split())
s = input()

# create a list of the number of ACs up to each index
ac_counts = [0]
for i in range(n):
    if s[i] == 'A' and s[i-1] == 'C':
        ac_counts.append(ac_counts[-1] + 1)
    else:
        ac_counts.append(ac_counts[-1])

# for each query, find the number of ACs in the substring
for i in range(q):
    l, r = map(int, input().split())
    print(ac_counts[r] - ac_counts[l-1])
