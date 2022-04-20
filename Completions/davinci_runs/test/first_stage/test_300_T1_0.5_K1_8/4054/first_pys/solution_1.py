

import sys

def main():
    input = sys.stdin.readlines()
    input = [int(x) for x in input[0].split()]
    output = 0
    for x in input:
        for y in input:
            if x != y:
                output += x + y
    print(output)

main()