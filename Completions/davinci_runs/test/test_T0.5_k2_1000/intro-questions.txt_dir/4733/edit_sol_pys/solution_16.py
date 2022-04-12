
import sys

def main():
    num_cases = int(sys.stdin.readline().strip())
    for i in range(num_cases):
        n = int(sys.stdin.readline().strip())
        shuffle = sys.stdin.readline().strip()

        if shuffle == 'out\n':
            print(n//2)
        else:
            print(n-1)

if __name__ == '__main__':
    main()
