

def main():
    try:
        expresion = input()
        result = eval(expresion)
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero")

if __name__ == "__main__":
    main()
