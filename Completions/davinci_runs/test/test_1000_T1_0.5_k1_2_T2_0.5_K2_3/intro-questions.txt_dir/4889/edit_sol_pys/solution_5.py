
import sys

def main():
    n = int(raw_input().strip())
    rods = []
    for i in range(n):
        rods.append(int(raw_input().strip()))
    rods.sort()
    while len(rods) > 1:
        rods[0] += rods.pop(-1)
        rods.sort()
    print(rods[0])

if __name__ == '__main__':
    main()
