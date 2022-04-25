

N = int(input())
M = int(input())
A = list(map(int, input().split()))

# N = 5
# M = 4
# A = [1, 4, 5, 60, 4]


def solution(N, M, A):
    # calculate prefix sums
    prefix_sums = [0]*(N+1)
    for i in range(N):
        prefix_sums[i+1] = prefix_sums[i] + A[i]

    # calculate prefix medians (average)
    prefix_medians = [0]*(N+1)
    for i in range(N):
        prefix_medians[i+1] = (prefix_sums[i+1] + i) // (i+1)

    # calculate suffix medians
    suffix_medians = [0]*(N+1)
    for i in range(N-1, -1, -1):
        suffix_medians[i] = (prefix_sums[N] - prefix_sums[i] + N-i-1) // (N-i)

    # calculate total number of pairs
    total_pairs = 0

    # calculate number of pairs with prefix medians
    prefix_medians_count = [0]*(N+1)
    for i in range(N+1):
        prefix_medians_count[i] = prefix_medians_count[i-1]
        if prefix_medians[i] == M:
            prefix_medians_count[i] += 1

    for i in range(N+1):
        total_pairs += prefix_medians_count[i]
        if suffix_medians[i] == M:
            total_pairs += prefix_medians_count[i]

    return total_pairs

print(solution(N, M, A))
