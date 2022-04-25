
import sys, math

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        m, k = line.split()
        m = int(m)
        k = int(k)
        if k == 1:
            print(1)
        else:
            print(int(math.ceil(m / k)))

if __name__ == "__main__":
    main()
