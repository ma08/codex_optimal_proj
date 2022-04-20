

def main():
    expression = input("Enter your expression")
    try:
        result = eval(expression)
        print(result)
    except:
        print("Syntax error")

if __name__ == "__main__":
    main()
