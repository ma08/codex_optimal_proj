
import sys

def main():
    n = int(sys.stdin.readline().strip())
    arr = [int(x) for x in sys.stdin.readline().strip().split()]
    min_val = min(arr)
    max_val = max(arr)
    print(min_val, max_val)

if __name__ == '__main__':
    main()
