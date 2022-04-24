

def find_nums(n):
    num1 = 1
    num2 = num1
    nums = set(input().split())
    for num in nums:
        if int(num) > num2:
            num2 *= int(num)
        elif int(num) > num1:
            num1 *= int(num)
    return num1, num2

def main():
    n = int(input())
    num1, num2 = find_nums(n)
    print(num1, num2)

if __name__ == "__main__":
    main()
