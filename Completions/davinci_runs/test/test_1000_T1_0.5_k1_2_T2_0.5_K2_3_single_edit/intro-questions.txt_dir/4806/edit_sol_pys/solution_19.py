

import sys

def main():
    lines = sys.stdin.readlines()
    moves = lines[0].strip()
    counter = ''
    for i in range(len(moves)):
        if moves[i] == 'R':
            counter += 'S'
        elif moves[i] == 'B':
            counter += 'K'
        elif moves[i] == 'L':
            counter += 'H'
        elif moves[i] == 'R' and moves[i+1] == 'R':
            counter += 'S'
        elif moves[i] == 'R' and moves[i+1] == 'B':
            counter += 'S'
        elif moves[i] == 'R' and moves[i+1] == 'L':
            counter += 'S'
        elif moves[i] == 'B' and moves[i+1] == 'R':
            counter += 'K'
        elif moves[i] == 'B' and moves[i+1] == 'B':
            counter += 'K'
        elif moves[i] == 'B' and moves[i+1] == 'L':
            counter += 'K'
        elif moves[i] == 'L' and moves[i+1] == 'R':
            counter += 'H'
        elif moves[i] == 'L' and moves[i+1] == 'B':
            counter += 'H'
        elif moves[i] == 'L' and moves[i+1] == 'L':
            counter += 'H'
        elif moves[i] == 'R' and moves[i+1] == 'R' and moves[i+2] == 'B':
            counter += 'C'
        elif moves[i] == 'R' and moves[i+1] == 'R' and moves[i+2] == 'L':
            counter += 'C'
        elif moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'R':
            counter += 'C'
        elif moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'B':
            counter += 'C'
        elif moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'L':
            counter += 'C'
        elif moves[i] == 'R' and moves[i+1] == 'L' and moves[i+2] == 'R':
            counter += 'C'
        elif moves[i] == 'R' and moves[i+1] == 'L' and moves[i+2] == 'B':
            counter += 'C'
        elif moves[i] == 'R' and moves[i+1] == 'L' and moves[i+2] == 'L':
            counter += 'C'
        elif moves[i] == 'B' and moves[i+1] == 'R' and moves[i+2] == 'R':
            counter += 'C'
        elif moves[i] == 'B' and moves[i+1] == 'R' and moves[i+2] == 'B':
            counter += 'C'
        elif moves[i] == 'B' and moves[i+1] == 'R' and moves[i+2] == 'L':
            counter += 'C'
        elif moves[i] == 'B' and moves[i+1] == 'B' and moves[i+2] == 'R':
            counter += 'C'
        elif moves[i] == 'B' and moves[i+1] == 'B' and moves[i+2] == 'B':
            counter += 'C'
        elif moves[i] == 'B' and moves[i+1] == 'B' and moves[i+2] == 'L':
            counter += 'C'
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
