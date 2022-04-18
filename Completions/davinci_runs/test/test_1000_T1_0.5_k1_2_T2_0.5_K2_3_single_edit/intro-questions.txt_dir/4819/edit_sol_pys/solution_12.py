

def main():
    # input
    nums = set()
    for i in range(10):
        num = int(input())
        num %= 42
        nums.add(num)

    # output
    print(len(nums))

if __name__ == "__main__":
    main()
