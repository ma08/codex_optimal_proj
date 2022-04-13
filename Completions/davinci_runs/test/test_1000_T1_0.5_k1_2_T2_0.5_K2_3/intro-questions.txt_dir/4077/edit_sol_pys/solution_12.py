

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
    # calculate prefix medians (left part)
    prefix_medians = [[0, 0] for _ in range(N+1)]
    for i in range(N+1):
        prefix_medians[i][0] = (prefix_sums[i] + i) // (i+1)
        prefix_medians[i][1] = prefix_medians[i-1][1]
        if prefix_medians[i][0] == M:
            prefix_medians[i][1] += 1

    # calculate suffix medians (right part)
    suffix_medians = [[0, 0] for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        suffix_medians[i][0] = (prefix_sums[N] - prefix_sums[i] + N-i-1) // (N-i)
        suffix_medians[i][1] = suffix_medians[i+1][1]
        if suffix_medians[i][0] == M:
            suffix_medians[i][1] += 1

    # calculate prefix sums
    prefix_sums = [0]*(N+1)
    for i in range(N):
        prefix_sums[i+1] = prefix_sums[i] + A[i]

    # calculate total number of pairs
    total_pairs = 0

    # calculate total number of pairs
    for i in range(N+1):
        total_pairs += prefix_medians[i][1] * suffix_medians[i+1][1]

    return total_pairs

print(solution(N, M, A))
