

import sys

def main():
    n = int(sys.stdin.readline())
    temperatures = sorted(list(map(int, sys.stdin.readline().split())))
    if temperatures[0] == temperatures[1] or temperatures[-2] == temperatures[-1] or temperatures[-2] - temperatures[0] < temperatures[-1] - temperatures[1]:
        return print("impossible")
    print(" ".join(map(str, reversed(temperatures))))

if __name__ == "__main__":
    main()
