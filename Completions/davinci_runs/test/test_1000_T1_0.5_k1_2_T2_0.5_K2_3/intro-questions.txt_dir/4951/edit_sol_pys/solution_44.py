

import sys

def main():
    lines = [sys.stdin.readline().strip().split(' -> ') for _ in range(int(sys.stdin.readline().strip()))]

    for i, line in enumerate(lines):
        if line[0] != '' and line[0] not in [j[1] for j in lines[:i]]:
            print(i+1)
            break
    else:
        print('correct')

main()
