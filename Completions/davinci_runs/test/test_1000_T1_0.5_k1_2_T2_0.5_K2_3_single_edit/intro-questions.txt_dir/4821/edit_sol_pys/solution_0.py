

from sys import stdin
from collections import Counter

def main():
    cards = stdin.readline().strip().split()
    if len(cards) % 2 != 0:
        print('GRESKA')
        return
    suits = Counter()
    for i in range(0, len(cards), 2):
        suits[cards[i + 1]] += int(cards[i])
    for i in ['P', 'K', 'H', 'T']:
        print(13 - suits[i], end=' ')

if __name__ == '__main__':
    main()
