

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] += 1
            nums[i + 1] += 1
    if len(set(nums)) == 1:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
