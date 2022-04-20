

n, q = map(int, input().split())
s = input()

# for each query, find the number of ACs in the substring
for i in range(q):
    l, r = map(int, input().split())
    print(s[l-1:r].count('AC'))
