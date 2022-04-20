

# input
N = int(input())
S = input()

# initialization
count = 0

# count
for i in range(N):
    if S[i:i+3] == "ABC":
        count += 1

# output
print(count)