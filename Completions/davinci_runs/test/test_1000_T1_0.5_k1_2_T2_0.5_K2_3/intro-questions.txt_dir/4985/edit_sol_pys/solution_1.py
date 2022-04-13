
import sys

def get_value(card):
    value = 0

    if card[0] == 'A':
        value = 11
    elif card[0] == 'K':
        value = 4
    elif card[0] == 'Q':
        value = 3
    elif card[0] == 'J':
        value = 20
    elif card[0] == 'T':
        value = 10
    elif card[0] == '9':
        value = 14
    elif card[0] == '8':
        value = 0
    elif card[0] == '7':
        value = 0
    else:
        print('Error')

    if card[1] == 'S' or card[1] == 'H':
        return value
    elif card[1] == 'D' or card[1] == 'C':
        return value // 2
    else:
        print('Error')

def main():
    data = sys.stdin.readline().split()
    num_hands = int(data[0])
    dominant_suit = data[1]

    total_points = 0
    for i in range(4 * num_hands):
        card = sys.stdin.readline().strip()
        total_points += get_value(card)

    print(total_points)

if __name__ == '__main__':
    main()
