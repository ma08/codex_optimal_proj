

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        print(nums[i] + nums[i + 1])

if __name__ == '__main__':
    main()
