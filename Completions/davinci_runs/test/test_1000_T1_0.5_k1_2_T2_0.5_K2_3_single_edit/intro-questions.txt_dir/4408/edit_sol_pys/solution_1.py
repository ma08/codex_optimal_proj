

import sys


def get_input():
    inputs = []
    for i in range(5):
        inputs.append(list(map(int, input().rstrip().split())))
    return inputs

def get_cards(cards, index, k):
    return cards[index*k:(index+1)*k]



def get_player_joy(cards, player_fav_numbers, joy_levels):
    fav_cards = [list(filter(lambda x: x == player_fav_number, cards)) for player_fav_number in player_fav_numbers]
    fav_cards = [len(cards) for cards in fav_cards]
    return sum(map(lambda x: joy_levels[x], fav_cards))



def main(n, k, cards, player_fav_numbers, joy_levels):
    return get_player_joy(get_cards(cards, n, k), player_fav_numbers, joy_levels)


if __name__ == '__main__':
    n, k = get_input()[0]
    cards = get_input()[1]
    player_fav_numbers = get_input()[2]
    joy_levels = get_input()[3]
    print(main(n, k, cards, player_fav_numbers, joy_levels))
