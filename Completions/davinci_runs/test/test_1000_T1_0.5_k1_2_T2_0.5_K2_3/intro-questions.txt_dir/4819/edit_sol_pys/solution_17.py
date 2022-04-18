
def main():
    nums = []
    for i in range(10):
        num = int(input())
        num %= 42
        nums.append(num)

    # output
    print(len(set(nums)))

if __name__ == "__main__":
    main()
