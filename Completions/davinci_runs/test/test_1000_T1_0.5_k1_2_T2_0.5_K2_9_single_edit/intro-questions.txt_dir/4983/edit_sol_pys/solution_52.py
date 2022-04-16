
x = int(input("Enter a number: "))

def product(x):
    if x < 10:
        return x
    else:
        y = 1
        for i in str(x):
            if int(i) != 0:
                y *= int(i)
        return product(y)

print("The result is: ", product(x))
