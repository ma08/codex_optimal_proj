from collections import Counter

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    counts = Counter(nums)
    max_num = max(counts)
    if counts[max_num] == 1:
        print(nums.index(max_num) + 1)
    print("none")

if __name__ == "__main__":
    main()
