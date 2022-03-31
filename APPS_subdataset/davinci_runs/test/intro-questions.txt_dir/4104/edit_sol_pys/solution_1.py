

def main():
    """
    The bug is that the last operand is not subtracted from the result.
    """
    expression = raw_input()
    result = 0
    for operand in expression.split('+'):
        result -= int(operand)
    print(result)

if __name__ == '__main__':
    main()
