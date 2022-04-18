

import sys

def main():
    n = int(sys.stdin.readline())
    temperatures = sorted(list(map(int, sys.stdin.readline().split())))
    if temperatures[0] != temperatures[1]:
        if temperatures[-2] != temperatures[-1]:
            if temperatures[-2] - temperatures[0] <= temperatures[-1] - temperatures[1]:
                print(" ".join(map(str, reversed(temperatures))))
                return
    print("impossible")

if __name__ == "__main__":
    main()
