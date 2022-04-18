

import sys

def main():
    lines = []
    for i in range(int(sys.stdin.readline().strip())):
        lines.append(sys.stdin.readline().strip().split(' -> '))

    for i, line in enumerate(lines):
        if line[0] != '' and line[0] not in [j[1] for j in lines[:i] if len(j) > 1]:
            print(i+1)
            break
    else:
        print('correct')

main()
