
n = int(input())

x = [0] * n
y = [0] * n

for i in range(n): 
    x[i], y[i] = map(int, input().split())
    
print(max(y) - min(x))
