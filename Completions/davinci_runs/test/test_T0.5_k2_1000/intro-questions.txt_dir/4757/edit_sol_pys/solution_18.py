
import sys

def main():
    n = int(sys.stdin.readline())
    e = int(sys.stdin.readline())
    bar = 1
    villagers = set(range(1, n + 1))
    for i in range(e):
        line = sys.stdin.readline().split()
        k = int(line[0])
        present = set([int(x) for x in line[1:]])
        if bar in present:
            villagers = present
        else:
            villagers = villagers.intersection(present)
    print('\n'.join([str(x) for x in sorted(villagers)]))

main()
