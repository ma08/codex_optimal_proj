

import sys

def main():
    cans = int(sys.stdin.readline())  # number of cans
    duras = [int(x) for x in sys.stdin.readline().split()]  # durations of cans
    shot = 0
    shotList = []
    for i in range(cans):
        shotList.append(i + 1)
    shotList.sort(key=lambda x: duras[x - 1])
    for i in range(cans):
        shot += (duras[shotList[i] - 1] * i + 1)
    print(shot)
    print(*shotList)

if __name__ == "__main__":
    main()
