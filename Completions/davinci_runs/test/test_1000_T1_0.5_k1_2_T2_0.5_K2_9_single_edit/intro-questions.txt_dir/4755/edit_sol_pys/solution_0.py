

# put your python code here
number, k = [int(x) for x in input().split()]
number -= number % (10**k)
print(number)
