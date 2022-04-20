

def main():
    expression = input("Enter an expression: ")
    values = [int(x) for x in expression.split('+')]
    print(sum(values))

main()
