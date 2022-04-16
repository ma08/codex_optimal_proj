def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    count = 0
    for i in range(n):
        if m - nums[i] >= 0:
            m -= nums[i]
            count += 1
        else:
            break
    print(count)



if __name__ == "__main__":
    main()
