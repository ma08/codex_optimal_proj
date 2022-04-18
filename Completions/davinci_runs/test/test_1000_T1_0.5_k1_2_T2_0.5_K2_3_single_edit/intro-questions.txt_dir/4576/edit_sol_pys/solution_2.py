

# get the input
n = int(input())
A = list(map(int, input().split()))

# initialize the number of pairs
num_pairs = 0

# loop over all pairs of i and j
for i in range(n):
    for j in range(i + 1, n):
        # check if A_i + A_j is even
        if (A[i] + A[j]) % 2 == 0:
            # increment the number of pairs
            num_pairs += 1

# print the number of pairs
print(num_pairs)
