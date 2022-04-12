
N, M = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

A.sort()
B.sort(reverse=True)

print('Yes' if sum(a * b for a, b in zip(A, B)) > 0 else 'No')
