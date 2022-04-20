
import sys

def main():
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    nums.sort()
    print(nums[-1])

if __name__ == "__main__":
    main()
