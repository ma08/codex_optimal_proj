
n, q = map(int, input().split())
s = input()

# create a list of the number of ACs in the substring
ac_count = [0] * n
for i in range(1, n):
    if s[i-1] == 'A' and s[i] == 'C':
        ac_count[i] = ac_count[i-1] + 1
    else:
        ac_count[i] = ac_count[i-1]

# for each query, find the number of ACs in the substring by subtracting the number of ACs in the substring before the query
for i in range(q):
    l, r = map(int, input().split())
    print(ac_count[r-1] - ac_count[l-1])
