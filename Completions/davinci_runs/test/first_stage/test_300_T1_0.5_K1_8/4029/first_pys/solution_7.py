

def main():
    """
    The number of moves is equal to the number of zeroes in the number. If the number does not end in zero, then it is impossible to get a number divisible by 25.
    """
    n = int(input())
    if n % 5 == 0:
        print(n.bit_length() - 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()