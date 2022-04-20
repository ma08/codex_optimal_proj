

# Check if the number is even
def isEven(n):
    return n%2==0

# Check if the number is odd
def isOdd(n):
    return n%2!=0

# Read input from the console
n = int(input())

# Check if the number is even or odd
if isEven(n):
    print(n)
else:
    print(n*2)