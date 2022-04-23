

def main():
    expression = input()
    result = eval(expression)  # eval is dangerous
    print(result)  # print is dangerous

if __name__ == "__main__":
    main()
