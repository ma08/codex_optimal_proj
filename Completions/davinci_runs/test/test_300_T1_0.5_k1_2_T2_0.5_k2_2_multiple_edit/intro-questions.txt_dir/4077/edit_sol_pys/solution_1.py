

# N = int(input())
# M = int(input())
# A = list(map(int, input().split()))

N = 5
M = 4
A = [1, 4, 5, 60, 4]

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
    # calculate prefix sums
    prefix_sums = [0]*(N+1)
    for i in range(N):
        prefix_sums[i+1] = prefix_sums[i] + A[i]

    # calculate prefix means
    prefix_means = [0]*(N+1) + [0]*(N+1)
    for i in range(N):
        prefix_means[i+1] = (prefix_sums[i+1] + i) // (i+1)

    # calculate suffix means
    suffix_means = [0]*(N+1) + [0]*(N+1)
    for i in range(N-1, -1, -1):
        suffix_means[i] = (prefix_sums[N] - prefix_sums[i] + N-i-1) // (N-i)

    # calculate total number of pairs
    total_pairs = 0

    # calculate number of pairs with prefix means
    prefix_means_count = [0]*(N+1) + [0]*(N+1)
    for i in range(N+1):
        prefix_means_count[i] = prefix_means_count[i-1]
        if prefix_means[i] == M:
            prefix_means_count[i] += 1

    for i in range(N+1):
        total_pairs += prefix_means_count[i]
        if suffix_means[i] == M:
            total_pairs += prefix_means_count[i]

    return total_pairs

print(solution(N, M, A))
