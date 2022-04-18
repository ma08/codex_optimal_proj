

import sys

def main():
    lines = sys.stdin.readlines()
    moves = lines[0].strip()
    counter = ''
    i = 0
    while i < len(moves):
        if moves[i] == 'R':
            counter += 'S'
        elif moves[i] == 'B':
            counter += 'K'
        elif moves[i] == 'L':
            counter += 'H'
        elif moves[i] == 'R' and moves[i+1] == 'R' and moves[i+2] == 'R' and i < len(moves) - 2:
            counter += 'S'
            i += 1
        elif moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'B' and i < len(moves) - 2:
            counter += 'S'
            i += 1
        elif moves[i] == 'R' and moves[i+1] == 'L' and moves[i+2] == 'L' and i < len(moves) - 2:
            counter += 'S'
            i += 1
        elif moves[i] == 'B' and moves[i+1] == 'R':
            counter += 'K'
            i += 1
        elif moves[i] == 'B' and moves[i+1] == 'B':
            counter += 'K'
            i += 1
        elif moves[i] == 'B' and moves[i+1] == 'L':
            counter += 'K'
            i += 1
        elif moves[i] == 'L' and moves[i+1] == 'R':
            counter += 'H'
            i += 1
        elif moves[i] == 'L' and moves[i+1] == 'B':
            counter += 'H'
            i += 1
        elif moves[i] == 'L' and moves[i+1] == 'L':
            counter += 'H'
            i += 1
        elif moves[i] == 'R' and moves[i+1] == 'R' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'R' and moves[i+1] == 'R' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        elif moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'R':
            counter += 'C'
            i += 3
        elif moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        elif moves[i] == 'R' and moves[i+1] == 'L' and moves[i+2] == 'R':
            counter += 'C'
            i += 3
        elif moves[i] == 'R' and moves[i+1] == 'L' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'R' and moves[i+1] == 'L' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'R' and moves[i+2] == 'R':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'R' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'R' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'B' and moves[i+2] == 'R':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'B' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'B' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'L' and moves[i+2] == 'R':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'L' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'B' and moves[i+1] == 'L' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'R' and moves[i+2] == 'R':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'R' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'R' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'B' and moves[i+2] == 'R':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'B' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'B' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'L' and moves[i+2] == 'R':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'L' and moves[i+2] == 'B':
            counter += 'C'
            i += 3
        elif moves[i] == 'L' and moves[i+1] == 'L' and moves[i+2] == 'L':
            counter += 'C'
            i += 3
        else:
            i += 1
    print(counter)

if __name__ == '__main__':
    main()
