
n, q = map(int, input().split())
s = input()

# create a list of the number of ACs in each substring
ac_counts = []
count = 0
for i in range(n):
    if s[i] == 'A' and i != n-1 and s[i+1] == 'C':
        count += 1
    ac_counts.append(count)

# for each query, find the number of ACs in the substring by subtracting the number of ACs in the previous substring
for i in range(q):
    l, r = map(int, input().split())
    print(ac_counts[r-1] - ac_counts[l-1])
