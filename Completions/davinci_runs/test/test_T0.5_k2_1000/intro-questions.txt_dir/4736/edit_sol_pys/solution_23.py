import sys

def get_input():
    """
    Reads the input from stdin and returns it as a list.

    :return: int[]
    """
    return list(map(int, input().strip().split()))

def get_cards(numbers):
    """
    Returns a list of cards based on the input list.

    :param numbers: int[]
    :return: int[]
    """
    cards = []
    for i in range(len(numbers)):
        cards += [i+1] * numbers[i]
    return cards

def get_num_combinations(cards, K):
    """
    Returns the number of combinations of the cards.

    :param cards: int[]
    :param K: int
    :return: int
    """
    return len(get_combinations(cards, K))

def get_combinations(cards, K):
    """
    Returns a list of combinations of the cards.

    :param cards: int[]
    :param K: int
    :return: int[]
    """
    if K == 1:
        return cards
    combinations = []
    for i in range(len(cards)):
        card = cards[i]
        sub_cards = cards[:i] + cards[i+1:]
        sub_combinations = get_combinations(sub_cards, K-1)
        for sub_combination in sub_combinations:
            if card < sub_combination[0]:
                combinations.append([card] + sub_combination)
    return combinations

def main():
    """
    Main function.
    """
    numbers = get_input()
    K = int(input().strip())
    cards = get_cards(numbers)
    num_combinations = get_num_combinations(cards, K)
    print(num_combinations)

if __name__ == "__main__":
    main()
