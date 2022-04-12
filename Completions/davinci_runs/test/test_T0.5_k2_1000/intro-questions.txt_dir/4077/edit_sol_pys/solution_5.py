

N = int(input())
M = int(input())
A = list(map(int, input().split()))

# N = 5
# M = 4
# A = [1, 4, 5, 60, 4]

# N = 3
# M = 1
# A = [1, 1, 1]

# N = 15
# M = 2
# A = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# N = 200000
# M = 100000
# A = [1]*N

# N = 200000
# M = 100000
# A = [i for i in range(1, N+1)]

# N = 200000
# M = 100000
# A = [i for i in range(N, 0, -1)]


def solution(N, M, A):
    # calculate prefix sums and prefix means
    prefix_sums = [0]*(N+1) # prefix sums
    prefix_means = [0]*(N+1) # prefix means
    for i in range(1, N+1):
        prefix_sums[i] = prefix_sums[i-1] + A[i-1]
        prefix_means[i] = (prefix_sums[i] + i) // i

    suffix_sums = [0]*(N+1)
    # calculate suffix means and suffix sums
    suffix_means = [0]*(N+1)
    for i in range(N-1, -1, -1):
        suffix_sums[i] = suffix_sums[i+1] + A[i]
        suffix_means[i] = (suffix_sums[i] + N-i) // (N-i)

    # calculate number of pairs with prefix means
    prefix_means_count = [0]*(N+1) # number of prefix means
    for i in range(1, N+1):
        prefix_means_count[i] = prefix_means_count[i-1]
        if prefix_means[i] == M:
            prefix_means_count[i] += 1

    # calculate number of pairs with prefix means
    # calculate number of pairs with suffix means
    total_pairs = 0 # total number of pairs
    for i in range(N+1): # number of pairs with suffix means
        if suffix_means[i] == M:
            total_pairs += prefix_means_count[i]
    return total_pairs

print(solution(N, M, A))
