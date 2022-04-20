#!/bin/python3



def main():
    # Read input, split it on a space and save the resulting list:
    a, b = [int(i) for i in input().split()]

    # Print the result
    print(a + b)

if __name__ == '__main__':
    main()
