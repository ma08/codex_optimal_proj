

def hailstone(n): #this is a recursive function that returns the value of n + n/2 + n/4 + n/8 ...
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + hailstone(n/2)
    else:
        return n + hailstone(3*n + 1)

n = int(input()) #takes in an integer as input
print(hailstone(n))
