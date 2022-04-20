

import sys

def main():
    N = int(sys.stdin.readline())
    A = [int(x) for x in sys.stdin.readline().split(' ')]
    B = [int(x) for x in sys.stdin.readline().split(' ')]
    B = [int(x) for x in sys.stdin.readline().split(' ')]
    # For each hero, we want to find the maximum number of monsters he/she can defeat.
    # We can do this by taking the minimum of the number of monsters attacking the town
    # they are in charge of and the number of monsters attacking the town to the right.
    # We then add the number of monsters the hero can defeat to our answer.

if __name__ == '__main__':
    main()
