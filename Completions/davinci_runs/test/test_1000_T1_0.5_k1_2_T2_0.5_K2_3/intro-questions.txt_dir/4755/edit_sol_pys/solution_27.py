

# put your python code here
a, b = [int(x) for x in input().split()]
a -= a % (10 * b)
print(a)
