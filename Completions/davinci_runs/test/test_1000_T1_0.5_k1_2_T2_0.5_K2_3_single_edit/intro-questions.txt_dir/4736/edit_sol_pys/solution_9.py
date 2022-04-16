import sys
import itertools

def get_input():
    """
    Reads the input from stdin and returns it as a list.

    :return: list
    """
    return list(map(int, sys.stdin.readline().strip().split()))

def get_cards(numbers):
    """
    Returns a list of cards based on the input list.

    :param numbers: list
    :return: list
    """
    cards = []
    for i in range(len(numbers)):
        cards += [i+1] * numbers[i]
    return cards

def get_num_permutations(cards, K):
    """
    Returns the number of permutations of the cards.

    :param cards: list
    :param K: int
    :return: int
    """
    return len(get_permutations(cards, K))

def get_permutations(cards, K):
    """
    Returns a list of permutations of the cards.

    :param cards: list
    :param K: int
    :return: list
    """
    if K == 1:
        return cards
    permutations = []
    for i in range(len(cards)):
        card = cards[i]
        sub_cards = cards[:i] + cards[i+1:]
        sub_permutations = get_permutations(sub_cards, K-1)
        for sub_permutation in sub_permutations:
            if card < sub_permutation[0]:
                permutations.append([card] + sub_permutation)
    return permutations

def get_num_permutations2(cards, K):
    """
    Returns the number of permutations of the cards.

    :param cards: list
    :param K: int
    :return: int
    """
    return len(list(itertools.permutations(cards, K)))

def main():
    """
    Main function.
    """
    numbers = get_input()
    K = int(sys.stdin.readline().strip())
    cards = get_cards(numbers)
    num_permutations = get_num_permutations2(cards, K)
    print(num_permutations)

if __name__ == "__main__":
    main()
