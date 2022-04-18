x = int(input())

def product(x):
    if x < 10: # if the number is less than 10, return the number
        return x
    else:
        y = 1
        for i in str(x): # if the number is greater than 10, loop through the number
            if int(i) != 0: # if the number is not zero, multiply it to the variable y
                y *= int(i)
        return product(y)
print(product(x))
