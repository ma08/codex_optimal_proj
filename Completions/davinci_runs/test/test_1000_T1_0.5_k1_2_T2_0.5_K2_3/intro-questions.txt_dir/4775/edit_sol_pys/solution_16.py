
import sys

def main():
    a, b = sys.stdin.readline().strip().split('\n')
    print(a)
    for i in range(len(b) - 1):
        print('.' * len(a))

if __name__ == "__main__":
    main()
