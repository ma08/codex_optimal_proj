
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        x = int(sys.stdin.readline().strip())
        k = 0
        while x > 1:
            k += 1
            x = x/2
        print(k)

if __name__ == '__main__':
    main()
