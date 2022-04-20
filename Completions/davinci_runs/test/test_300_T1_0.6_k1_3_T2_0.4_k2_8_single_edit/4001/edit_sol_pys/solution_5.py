

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def get_diff(s1, s2):
    return list(set(s1) - set(s2))

def find_nums(n):
    num1 = num2 = 1
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
