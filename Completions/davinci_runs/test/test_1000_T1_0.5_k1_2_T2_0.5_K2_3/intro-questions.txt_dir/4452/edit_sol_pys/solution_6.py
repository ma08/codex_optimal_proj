

import sys

def get_round_numbers(n, round_numbers=[]):
    num = n
    while num > 0:
        r_num = (num // 10) * 10
        round_numbers.append(r_num)
        num = num - r_num
    return round_numbers

    # get number of test cases
def main():
    t = int(sys.stdin.readline().strip())
        # get number of round numbers
    for i in range(t):
        # get list of round numbers
        n = int(sys.stdin.readline().strip())
        # print number of round numbers
        round_numbers = get_round_numbers(n)
        # print list of round numbers
        print(len(round_numbers))
        print(*round_numbers)

if __name__ == '__main__':
    main()
