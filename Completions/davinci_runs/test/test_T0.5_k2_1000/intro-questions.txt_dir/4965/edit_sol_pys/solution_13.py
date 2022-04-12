
import sys

def main():
    n = int(sys.stdin.readline())
    temperatures = list(map(int, sys.stdin.readline().split()))
    if temperatures[0] == temperatures[1] or temperatures[-2] == temperatures[-1] or temperatures[-2] - temperatures[0] < temperatures[-1] - temperatures[1]:
        print("impossible")
        return
    print(" ".join(map(str, sorted(temperatures, reverse=True))))

if __name__ == "__main__":
    main()
