
import sys

def main():
    expression = sys.stdin.readline().strip()
    operands = [float(x) for x in expression.split('+')]
    result = 0
    for operand in operands:
        result += operand
    print(f'{result:.2f}')

if __name__ == "__main__":
    main()
