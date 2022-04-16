

def stairways(nums):
    count = 0
    prev = None
    stairways = []
    for i in range(1, len(nums)):
        if prev is None:
            count += 1
            prev = nums[i]
        elif nums[i] != prev:
            stairways.append(count)
            count = 0
            prev = nums[i]
        else:
            count += 1
    stairways.append(count)
    return len(stairways), *stairways

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(*stairways(nums))

if __name__ == "__main__":
    main()
