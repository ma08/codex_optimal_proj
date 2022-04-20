

def find_nums(n):
    num1 = 1
    num2 = 1
    nums = set(input().split()) # чтение из файла
    for num in nums:
        if num1 > num2:
            num2 *= int(num)
        else:
            num1 *= int(num)
    return num1, num2

def main():
    n = int(input()) # чтение из файла
    num1, num2 = find_nums(n)
    print(num1, num2) # вывод в файл

if __name__ == "__main__":
    main()
