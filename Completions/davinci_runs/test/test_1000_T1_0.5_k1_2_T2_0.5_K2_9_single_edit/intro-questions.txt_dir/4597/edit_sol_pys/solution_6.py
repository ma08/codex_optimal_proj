
import sys

def main():
    n = int(sys.stdin.readline())

    # input
    nums = list(map(int, sys.stdin.readline().split()))

    # output
    print(nums[0] + nums[1])

if __name__ == '__main__':
    main()
