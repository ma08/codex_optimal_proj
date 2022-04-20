
# input
N, Q = map(int, input().split())
S = input()

# initialize
count = 0
ans = []

# count the number of ACs
for i in range(N-1):
    if S[i] == 'A' and S[i+1] == 'C':
        count += 1

# append the number of ACs to the list
ans.append(count)

# count the number of ACs in the substring
for i in range(Q):
    l, r = map(int, input().split())
    if S[l-1] == 'A' and S[l] == 'C' and S[r-2] == 'A' and S[r-1] == 'C':
        ans.append(count - 2)
    elif S[l-1] == 'A' and S[l] == 'C':
        ans.append(count - 1 + (r-l))
    elif S[r-2] == 'A' and S[r-1] == 'C':
        ans.append(count - 1)
    else:
        ans.append(count + (r-l))

# output
for i in range(Q):
    print(ans[i])
