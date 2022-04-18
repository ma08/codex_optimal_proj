

a = int(input("Enter the first number: "))
op = input("Enter the operator: ")
b = int(input("Enter the second number: "))

if op == '+':
    print("The sum is: ", a+b)
elif op == '*':
    print("The product is: ", a*b)
else:
    print("Invalid operator")
