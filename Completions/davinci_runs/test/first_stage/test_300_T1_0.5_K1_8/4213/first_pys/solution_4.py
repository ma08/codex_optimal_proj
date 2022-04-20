

N = int(input())
A = list(map(int, input().split()))

max_a = max(A)
min_a = min(A)

print(max(max_a-min_a, max_a-min(A[:A.index(max_a)]), max(A[A.index(min_a)+1:])-min_a))