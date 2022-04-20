import sys

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    if max(nums) < sum(nums) - max(nums):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
