

from sys import stdin
from collections import Counter, defaultdict

def main():
    cards = stdin.readline().strip()
    if len(cards) % 3 != 0:
        print('GRESKA')

        return
    numbers = defaultdict(list)
    suits = Counter()
    for i in range(0, len(cards), 3):
        numbers[cards[i+1]].append(cards[i+2])

        suits[cards[i]] += 1
    for i in ['P', 'K', 'H', 'T']:
        print(13 - suits[i], end=' ')

if __name__ == '__main__':
    main()
