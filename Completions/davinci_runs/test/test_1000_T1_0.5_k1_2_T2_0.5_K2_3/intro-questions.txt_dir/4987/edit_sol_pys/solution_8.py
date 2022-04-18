def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    prev = nums[0]
    for i in range(1, n):
        if nums[i] - prev == 0:
            print("NO")
            return
        prev = nums[i]
    print("YES")


if __name__ == "__main__":
    main()


def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    prev = nums[0]
    for i in range(1, n):
        if nums[i] - prev == 0:
            print("NO")
            return
        prev = nums[i]
    print("YES")


if __name__ == "__main__":
    main()
