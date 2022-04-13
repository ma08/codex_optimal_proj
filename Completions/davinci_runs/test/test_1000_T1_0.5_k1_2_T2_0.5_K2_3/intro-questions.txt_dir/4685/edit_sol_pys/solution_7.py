
a, b, c = map(int, input().split())
k = int(input()) 
print(a * 2 ** k + b * 2 ** (k // 2) + c * 2 ** (k // 3))
