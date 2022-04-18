"""
This is a sample program for the first task in the first week of the
"Python Programming Essentials" course by Pirple.
"""

import sys

def main():
    """
    This is the main function of the program.
    """
    sheep, wolves = map(int, input().split())
    if sheep <= wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
