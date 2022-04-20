

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    while len(nums) > 1:
        a, b = nums[0], nums[1]
        if a == b:
            nums.remove(a)
        elif a * 2 == b:
            nums.remove(a)
            nums.remove(b)
        elif a * 3 == b:
            nums.remove(a)
            nums.remove(b)
        else:
            print("NO")
            return
    print("YES")
    return

if __name__ == "__main__":
    main()