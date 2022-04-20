
# input
N, Q = map(int, input().split())
S = input()

# initialize the list
count = [0]
ans = []

# count the number of ACs in the substring
for i in range(N):
    if i != 0:
        count.append(count[i-1])
    if S[i] == 'C':
        count[i] += 1

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
