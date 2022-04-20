import sys

def main():
    expression = sys.stdin.readline().strip()
    operands = [int(x) for x in expression.split("+")]
    result = 0
    for operand in operands:
        result += operand
    print(result)

if __name__ == "__main__":
    main()
