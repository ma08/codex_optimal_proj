

n, q = map(int, input().split())
s = input()

# # create a list of the indices of where AC occurs
# ac_indices = []
# for i in range(n-1):
#     if s[i] == 'A' and s[i+1] == 'C':
#         ac_indices.append(i)

# # for each query, find the number of ACs in the substring
# for i in range(q):
#     l, r = map(int, input().split())
#     count = 0
#     for j in ac_indices:
#         if l <= j+1 <= r:
#             count += 1
#     print(count)

# create a list of the number of ACs in each substring
ac_count = [0] * (n+1)
for i in range(n):
    if s[i:i+2] == 'AC':
        ac_count[i+1] = ac_count[i] + 1
    else:
        ac_count[i+1] = ac_count[i]

# for each query, print the difference in AC counts
for _ in range(q):
    l, r = map(int, input().split())
    print(ac_count[r-1] - ac_count[l-1])
