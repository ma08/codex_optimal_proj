

def main():
    expr = input()
    result = 0
    for i in range(len(expr)):
        if expr[i] == '+':
            result += int(expr[i+1])
        elif expr[i] == '-':
            result -= int(expr[i+1])
    print(result)

if __name__ == '__main__':
    main()