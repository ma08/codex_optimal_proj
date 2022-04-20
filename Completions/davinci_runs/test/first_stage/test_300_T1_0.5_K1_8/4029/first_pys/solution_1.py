

import sys

def main():
    n = input()
    digits = list(n)
    moves = 0
    while len(digits) > 2:
        if int(digits[-2]) % 2 == 0:
            digits = digits[:-2]
        else:
            digits = digits[:-1]
        moves += 1
    if int(digits[0]) % 5 == 0:
        print(moves)
    else:
        print(-1)

if __name__ == "__main__":
    main()