

# N days of vacation, M assignments
N, M = map(int, input().split())
A = list(map(int, input().split()))

# sort assignments by descending order
A.sort(reverse=True)

# can he finish all assignments?
if sum(A) > N:
    print(-1)
    exit()

# answer: N - sum(A)
print(N - sum(A))