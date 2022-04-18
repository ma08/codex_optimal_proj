
N = int(input())
A = list(map(int, input().split()))

max_a = max(A)
for a in A:
    print(max_a if a != max_a else max(A) - 1) 
