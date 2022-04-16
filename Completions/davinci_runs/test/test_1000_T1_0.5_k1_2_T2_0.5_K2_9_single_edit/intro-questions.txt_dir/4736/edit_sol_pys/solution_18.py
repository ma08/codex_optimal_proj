

def get_num_ways(cards, k):
    if k == 1:
        return sum(cards)

    if k == 2:
        return sum(cards) * (sum(cards) - 1)

    if k == 3:
        return sum(cards) * (sum(cards) - 1) * (sum(cards) - 2)

    return cards[0] * get_num_ways(cards[1:], k - 1)

if __name__ == "__main__":
    cards = [int(i) for i in input().split()]
    k = int(input())
    print(get_num_ways(cards, k))
