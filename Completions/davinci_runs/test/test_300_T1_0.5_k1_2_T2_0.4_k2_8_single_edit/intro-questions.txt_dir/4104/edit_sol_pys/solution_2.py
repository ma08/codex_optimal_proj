

def main():
    expression = input("Enter the expression: ")
    try:
        result = eval(expression)
        print(result)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
