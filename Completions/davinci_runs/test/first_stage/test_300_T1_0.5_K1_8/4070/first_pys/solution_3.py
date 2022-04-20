

import sys

def main():
    n = int(input())
    number_of_ones = 0
    for i in range(0, n):
        if i % 2 == 0:
            number_of_ones += 1
        else:
            number_of_ones -= 1
    if number_of_ones < 0:
        number_of_ones = 0
    print(number_of_ones)

if __name__ == "__main__":
    main()