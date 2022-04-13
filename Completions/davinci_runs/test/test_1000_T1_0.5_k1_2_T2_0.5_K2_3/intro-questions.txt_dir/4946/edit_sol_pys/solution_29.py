

def main():
    n = int(input())
    nums = [int(i) for i in input().split()]
    seen = {}
    min_dist = n
    for i, num in enumerate(nums):
        if num in seen.keys():
            min_dist = min(min_dist, i - seen[num])
        seen[num] = i
    return min_dist

if __name__ == "__main__":
    print(main())
