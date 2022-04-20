

import sys

def is_lucky(n):
    n = str(n)
    first_half = sum([int(i) for i in n[:len(n)//2]])  # sum of first half
    second_half = sum([int(i) for i in n[len(n)//2:]])  # sum of second half
    if first_half == second_half:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    n = sys.stdin.read().strip()
    print(is_lucky(n))
