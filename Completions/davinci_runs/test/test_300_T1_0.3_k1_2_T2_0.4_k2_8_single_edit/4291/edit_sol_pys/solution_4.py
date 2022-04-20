

n, q = map(int, input().split())
s = input()

# create a list of the number of ACs in the substring
ac_counts = []
count = 0
for i in range(n):
    if s[i] == 'C':
        count = 0
    elif s[i] == 'A':
        count += 1
    ac_counts.append(count)

# for each query, find the number of ACs in the substring
for i in range(q):
    l, r = map(int, input().split())
    print(ac_counts[r-1] - ac_counts[l-1])
