
import sys

def main():
    n = int(sys.stdin.readline().strip())
    arr = [int(x) for x in sys.stdin.readline().strip().split()]
    arr.sort()
    count = 0
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
