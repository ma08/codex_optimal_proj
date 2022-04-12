
import sys

def get_rounded_numbers(n):
    rounded_numbers = []
    num = n
    while num > 0:
        rn = (num // 10) * 10
        rounded_numbers.append(rn)
        num -= rn
    return rounded_numbers

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        rounded_numbers = get_rounded_numbers(n)
        print(len(rounded_numbers))
        print(*rounded_numbers)

if __name__ == '__main__':
    main()
