

# Read input 
a, b, c = map(int, input().split())

# Compute the three values and print the maximum
print(max(a+b+c, a*b*c, (a+b)*c, a*(b+c)))
