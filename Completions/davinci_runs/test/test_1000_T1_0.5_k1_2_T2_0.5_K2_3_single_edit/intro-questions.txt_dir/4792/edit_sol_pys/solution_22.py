

import sys

def main():
    name = sys.stdin.readline().strip()
    compact = name[0] + name[1]
    for i in range(1, len(name)):
        if name[i] != compact[-1] and name[i] != compact[-2]:
            compact += name[i]
    print(compact)

main()
