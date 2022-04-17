

def main():
    expression = input()
    result = eval(expression)  # pylint: disable=eval-used
    print(result)

if __name__ == "__main__":
    main()
