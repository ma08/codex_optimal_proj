

a = int(input("Enter first number: "))
op = input("Enter operation: ")
b = int(input("Enter second number: "))

if op == "+":
    print("Result: ", a + b)
elif op == "*":
    print("Result: ", a * b)
elif op == "-":
    print("Result: ", a - b)
elif op == "/":
    print("Result: ", a / b)
else:
    print("Error")
