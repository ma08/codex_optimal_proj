

def find_nums(n):
    num1, num2 = 1, 1
    nums = set(input().split())
    for num in nums:
        if num1 > num2:
            num2 *= int(num)
        else:
            num1 *= int(num)
    return num1, num2

def main():
    n = int(input())
    num1, num2 = find_nums(n)
    print(num1, num2)

if __name__ == "__main__":
    main()
