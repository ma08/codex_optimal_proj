
import sys

def main():
    n = int(sys.stdin.readline().strip())
    numbers = []
    for i in range(n):
        numbers.append(int(sys.stdin.readline().strip()))
    numbers = set(numbers)  # 去重
    if len(numbers) == max(numbers):  # 判断是否有重复数字
        print("good job")
    else:
        for i in range(1, max(numbers) + 1):
            if i not in numbers:
                print(i)

if __name__ == '__main__':
    main()
