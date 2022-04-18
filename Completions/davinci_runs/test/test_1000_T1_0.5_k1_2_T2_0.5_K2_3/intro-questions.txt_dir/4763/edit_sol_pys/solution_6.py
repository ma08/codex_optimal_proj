import sys

def main():
    n = int(sys.stdin.readline())
    if n <= 60:
        print("impossible")
        return

    num_triples = min(n // 60, 3)
    n -= num_triples * 60

    num_doubles = min(n // 30, 3-num_triples)
    n -= num_doubles * 30

    num_singles = min(n // 10, 3-num_triples-num_doubles)
    n -= num_singles * 10

    if n != 0:
        print("impossible")
        return

    for i in range(num_triples):
        print("triple 20")
    for i in range(num_doubles):
        print("double 20")
    for i in range(num_singles):
        print("single 20")

if __name__ == '__main__':
    main()


import sys

def main():
    n = int(sys.stdin.readline())

    if n <= 60:
        print("impossible")
        return

    # Find the largest number of triples that can be used.
    num_triples = min(n // 60, 3)
    n -= num_triples * 60  # Remove the triples from the total.

    # Find the largest number of doubles that can be used.
    num_doubles = min(n // 30, 3-num_triples)
    n -= num_doubles * 30  # Remove the doubles from the total.

    # Find the largest number of singles that can be used.
    num_singles = min(n // 10, 3-num_triples-num_doubles)
    n -= num_singles * 10  # Remove the singles from the total.

    # If n is not 0, then we have not used all the darts.
    if n != 0:
        print("impossible")
        return

    for i in range(num_triples):
        print("triple 20")
    for i in range(num_doubles):
        print("double 20")
    for i in range(num_singles):
        print("single 20")

if __name__ == '__main__':
    main()
