

def main():
    expression = input()
    result = sum(map(int, expression.split('+')))
    print(result)

main()
