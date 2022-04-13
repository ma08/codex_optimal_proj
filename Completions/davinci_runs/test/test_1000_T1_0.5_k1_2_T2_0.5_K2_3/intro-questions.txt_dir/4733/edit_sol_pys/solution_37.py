
import sys

def main():
    num_cases = int(sys.stdin.readline().strip())
    for i in range(num_cases):
        n = int(sys.stdin.readline().strip())
        shuffle = sys.stdin.readline().strip()

        print(n//2)

if __name__ == '__main__':
    main()
