

def stairways(n, nums):
    stairways = [1]
    for i in range(n-1):
        if nums[i] != nums[i+1]:
            stairways.append(1)
        else: stairways[-1] += 1
    return len(stairways), stairways, nums

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(*stairways(nums))

if __name__ == "__main__":
    main()
