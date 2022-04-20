
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = []
for i in range(n): 
    result.append((a[i] + b[i]) % n)
print(" ".join(map(str, result)))
