

import sys
sys.setrecursionlimit(100000)
def get_input():
    inputs = []
    for i in range(4):
        inputs.append(list(map(int, input().split())))
    return inputs

def get_cards(cards, index, k):
    return cards[index*k:(index+1)*k]


def get_player_joy(cards, player_fav_number, joy_levels):
    fav_cards = list(filter(lambda x: x == player_fav_number, cards))
    return joy_levels[len(fav_cards)]

def main():
    n, k = get_input()[0]
    cards = get_input()[1]
    player_fav_number = get_input()[2]
    joy_levels = get_input()[3]
    max_joy = 0
    for i in range(n):
        max_joy += get_player_joy(get_cards(cards, i, k), player_fav_number[i], joy_levels)
    print(max_joy)


if __name__ == "__main__":
    main()
