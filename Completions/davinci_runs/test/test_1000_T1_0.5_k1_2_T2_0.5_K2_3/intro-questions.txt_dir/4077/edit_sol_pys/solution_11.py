
N = 5
M = 4
A = [1, 4, 5, 60, 4]

def solution(N, M, A):
    prefix_sums = [0] * (N + 1)
    for i in range(N):
        prefix_sums[i+1] = prefix_sums[i] + A[i]

    prefix_means = [0] * (N + 1)
    for i in range(N):
        prefix_means[i+1] = (prefix_sums[i+1] + i) // (i+1)

        prefix_means[i+1] = (prefix_sums[i+1] + i) // (i+1)

    suffix_means = [0] * (N + 1)
    for i in range(N-1, -1, -1):
        suffix_means[i] = (prefix_sums[N] - prefix_sums[i] + N-i-1) // (N-i)

    total_pairs = 0

    prefix_means_count = [0] * (N + 1)
    for i in range(N+1):
        prefix_means_count[i] = prefix_means_count[i-1]
        if prefix_means[i] == M:
            prefix_means_count[i] += 1

    for i in range(N):
        total_pairs += prefix_means_count[i]
        if suffix_means[i] == M:
            total_pairs += prefix_means_count[i]


    return total_pairs

print(solution(N, M, A))
