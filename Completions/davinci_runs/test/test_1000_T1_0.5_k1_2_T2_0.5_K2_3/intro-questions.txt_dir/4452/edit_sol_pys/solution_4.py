
import sys

def get_round_nums(n):
    round_nums = [0]
    num = n
    while num > 0:
        rn = (num // 10) * 10 + 10
        round_nums.append(rn)
        num = num - rn + 10
    return round_nums

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        round_nums = get_round_nums(n)
        print(len(round_nums))
        print(*round_nums)

if __name__ == '__main__':
    main()
