
import itertools

num_cards = [int(x) for x in input().split()]
k = int(input())

def is_ascending(lst):
    return all(lst[i] < lst[i+1] for i in range(len(lst)-1))

def count_ascending(deck, k):
    count = 0
    for hand in itertools.combinations(deck, k):
        if is_ascending(hand):
            count += 1
    return count

print(count_ascending(num_cards, k))
