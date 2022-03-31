

import math
import sys

def get_number_of_possible_triples(n):
    number_of_triples = 0
    for a in range(1, math.ceil(math.sqrt(n))):
        b = (n - a) / (a + 1)
        if b == int(b):
            number_of_triples += 1
    return number_of_triples

def main():
    n = int(input())
    print(get_number_of_possible_triples(n))

if __name__ == '__main__':
    main()
