
import sys

def main():
    a, b = sys.stdin.readline().strip().split()
    for i in range(len(b)):
        if b[i] in a:
            for j in range(i):
                print('.' * len(a))
            print(a)
            for j in range(i+1, len(b)):
                print('.' * len(a))
            break

if __name__ == "__main__":
    main()
