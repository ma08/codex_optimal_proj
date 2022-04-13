

def main():
    num = int(input())
    nums = []
    for i in range(num):
        nums.append(int(input()))
    total = 0
    for i in nums:
        if 10 <= i < 100: # 10-99
            total += i % 10
        elif 100 <= i < 1000: # 100-999
            total += (i // 100) ** 2
        elif 1000 <= i < 10000: # 1000-9999
            total += (i // 1000) ** 3
    print(total)

if __name__ == '__main__':
    main()
