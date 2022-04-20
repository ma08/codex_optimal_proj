

def main():
    expression = input()
    result = eval(expression.replace("^", "**"))
    print(result)

if __name__ == "__main__":
    main()
