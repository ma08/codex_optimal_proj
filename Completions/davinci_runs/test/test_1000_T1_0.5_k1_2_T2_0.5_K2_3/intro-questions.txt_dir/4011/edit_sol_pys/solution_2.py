
import sys

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    fs = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(len(nums)):
        nums[i] = fs[nums[i]-1]
    print(''.join(map(str, nums)))


if __name__ == '__main__':
    main()
