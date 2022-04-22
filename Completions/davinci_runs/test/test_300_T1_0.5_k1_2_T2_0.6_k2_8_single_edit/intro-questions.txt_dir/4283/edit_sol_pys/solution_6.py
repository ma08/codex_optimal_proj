def main():
    n, k = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        if nums[i] >= nums[k-1] and nums[i] > 0:
            count += 1
    print(count)




if __name__ == '__main__':
    main()
