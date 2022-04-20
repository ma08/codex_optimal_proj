# ABC085C - Otoshidama

# input
N, Q = map(int, input().split())
S = input()

# initialize
count = 0
ans = []

# count the number of ACs in the substring
for i in range(Q):
    l, r = map(int, input().split())
    for j in range(l-1, r-1):
        if S[j] == 'A' and S[j+1] == 'C':
            count += 1

# append the number of ACs to the list
ans.append(count)

# count the number of ACs in the substring
for i in range(Q):
    l, r = map(int, input().split())
    if S[l-1] == 'A' and S[l] == 'C':
        ans.append(count - 1)
    else:
        ans.append(count)

# output
for i in range(Q):
    print(ans[i])
