

import sys
sys.setrecursionlimit(100000)

def get_input(n):
    return list(map(int, input().split()))[:n]

def get_cards(cards, index, k):
    return cards[index*k:(index+1)*k]


def get_player_joy(cards, player_favorite_number, joy_levels):
    fav_cards = list(filter(lambda x: x == player_favorite_number, cards))
    return joy_levels[len(fav_cards)]

def main():
    n, k = get_input(2)
    cards = get_input(n*k)
    player_favorite_numbers = get_input(n)
    joy_levels = get_input(k)
    max_joy = 0
    for i in range(n):
        max_joy += get_player_joy(get_cards(cards, i, k), player_favorite_numbers[i], joy_levels)
    print(max_joy)


if __name__ == "__main__":
    main()
