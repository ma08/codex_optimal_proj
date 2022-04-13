

import sys

def main():
    program = sys.stdin.read().strip()
    nop_needed = 0 # nop needed to align
    while program:
        if len(program) % 4 == 0:
            program = program[4:]
        else:
            program = program[1:]
            nop_needed += 1
    print(nop_needed)

main()
