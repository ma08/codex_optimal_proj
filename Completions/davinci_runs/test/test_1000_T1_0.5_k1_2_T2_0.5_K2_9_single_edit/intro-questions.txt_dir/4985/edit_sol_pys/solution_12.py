

import sys



class Card:
    def __init__(self, card):
        self.value = 0
        self.value = self.get_value(card)

    def get_value(self, card):
        if card[0] == 'A':
            self.value = 11
        elif card[0] == 'K':
            self.value = 4
        elif card[0] == 'Q':
            self.value = 3
        elif card[0] == 'J':
            self.value = 20
        elif card[0] == 'T':
            self.value = 10
        elif card[0] == '9':
            self.value = 14
        elif card[0] == '8':
            self.value = 0
        elif card[0] == '7':
            self.value = 0
        else:
            print('Error')

        if card[1] == 'S' or card[1] == 'H':
            return self.value
        elif card[1] == 'D' or card[1] == 'C':
            return self.value // 2
        else:
            print('Error')


def main():
    data = sys.stdin.readline().split()
    num_hands = int(data[0])
    dominant_suit = data[1]

    total_points = 0
    for i in range(4 * num_hands):
        card = sys.stdin.readline().strip()
        total_points += Card(card).value

    print(total_points)
    
    print(total_points)

if __name__ == '__main__':
    main()
