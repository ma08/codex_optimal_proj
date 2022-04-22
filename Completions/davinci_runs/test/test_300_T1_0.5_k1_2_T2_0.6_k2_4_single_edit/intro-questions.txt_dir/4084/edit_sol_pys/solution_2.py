

n = int(input())
a = list(map(int,input().split()))

max_a = max(a)
min_a = min(a)
sum_a = sum(a)

print(max_a - min_a, end=" ")

if max_a == min_a:
    print(n * (n - 1) // 2)
else: 
    print(max_a, min_a, sum_a)
