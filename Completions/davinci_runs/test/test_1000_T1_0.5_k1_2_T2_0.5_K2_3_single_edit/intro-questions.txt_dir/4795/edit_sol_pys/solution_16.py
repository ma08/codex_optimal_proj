

def main():
    num = int(input())
    nums = []
    for i in range(num):
        nums.append(int(input()))
    total = 0
    for i in nums:
        if i >= 10 and i < 100:
            total += i % 10
        elif i >= 100 and i < 1000:
            total += i // 100 + (i % 100) // 10 + (i % 10)
        elif i >= 1000 and i < 10000:
            total += i // 1000 + (i % 1000) // 100 + (i % 100) // 10 + (i % 10)
    print(total)

if __name__ == '__main__':
    main()
