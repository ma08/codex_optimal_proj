

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
    # calculate prefix sum
    prefix_sum = [0]*(N+1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + A[i]

    # calculate prefix median
    prefix_median = [0]*(N+1)
    for i in range(N):
        prefix_median[i+1] = (prefix_sum[i+1] + i) // (i+1)

    suffix_median = [0]*(N+1)
    for i in range(N-1, -1, -1):
        suffix_median[i] = (prefix_sum[N] - prefix_sum[i] + N-i-1) // (N-i)

    # calculate total number of pairs
    total_pairs = 0

    # calculate number of pairs with prefix median
    prefix_median_count = [0]*(N+1)
    for i in range(N+1):
        prefix_median_count[i] = prefix_median_count[i-1]
        if prefix_median[i] == M:
            prefix_median_count[i] += 1

    for i in range(N+1):
        total_pairs += prefix_median_count[i]
        if suffix_median[i] == M:
            total_pairs += prefix_median_count[i]

    return total_pairs

print(solution(N, M, A))
