
import sys


def get_round_numbers(number):
    round_numbers_list = []
    number_of_rounds = number
    while number_of_rounds > 0:
        round_number = (number_of_rounds // 10) * 10
        round_numbers_list.append(round_number)
        number_of_rounds = number_of_rounds - round_number
    return round_numbers_list


def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        round_numbers = get_round_numbers(n)
        print(len(round_numbers))
        print(*round_numbers)

if __name__ == '__main__':
    main()
