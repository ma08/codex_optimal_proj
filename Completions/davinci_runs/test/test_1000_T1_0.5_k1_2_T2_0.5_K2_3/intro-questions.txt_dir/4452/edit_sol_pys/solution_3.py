import sys

def get_round_numbers(n, round_numbers = []):
    num = n
    while num > 0:
        r_num = (num // 10) * 10
        round_numbers.append(r_num)
        num = num - r_num
    return round_numbers

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        round_numbers = get_round_numbers(n)
        print(len(round_numbers))
        print(*round_numbers)

if __name__ == '__main__':
    main()
