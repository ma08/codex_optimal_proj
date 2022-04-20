

# Read input x, a, b
x, a, b = map(int, input().split())

# Print 0 if x < a, else print b - a
if x < a: 
    print(0) 
else:
    print(b - a)
