
import sys

def main():
    lines = []
    for _ in range(int(sys.stdin.readline().strip())):
        lines.append(sys.stdin.readline().strip().split(' -> '))

    for idx, line in enumerate(lines):
        if line[0] != '' and line[0] not in [j[1] for j in lines[:idx]]:
            print(idx+1)
            break
    else:
        print('correct')

main()
