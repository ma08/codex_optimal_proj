

a, b, k = map(int, input().split())

for i in range(k):
    if a > b:
        a -= 1 
    else:
        b -= 1 

print(a, b)
