
import sys

def main():
    cans = int(sys.stdin.readline())
    duras = [int(x) for x in sys.stdin.readline().split()]
    shot = 0
    shotList = []
    for i in range(1, cans+1):
        shotList.append(i)
    shotList.sort(key=lambda x: duras[x-1], reverse=True)
    for i in range(1, cans+1):
        shot += (duras[shotList[i-1]-1]*i)
    print(shot)
    print(*shotList)

if __name__ == "__main__":
    main()
