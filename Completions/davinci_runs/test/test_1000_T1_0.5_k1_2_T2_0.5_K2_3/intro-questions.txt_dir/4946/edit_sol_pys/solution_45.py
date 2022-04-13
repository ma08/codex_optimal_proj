

def main():
    n = int(input())
    nums = [int(i) for i in input().split()]
    seen = {}
    min_dist = n
    for i, num in enumerate(nums):
        if num not in seen:
            seen[num] = i
        else:
            min_dist = min(min_dist, i - seen[num] + 1)
    return min_dist if min_dist < n else -1

if __name__ == "__main__":
    print(main())
