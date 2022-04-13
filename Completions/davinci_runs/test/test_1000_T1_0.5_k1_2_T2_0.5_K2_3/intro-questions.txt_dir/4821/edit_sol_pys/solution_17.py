

from sys import stdin
from collections import Counter

def main():
    cards = stdin.readline().strip()
    if len(cards) % 3 != 0:
        print('GRESKAAAA')
        return
    suits = Counter()
    for i in range(0, len(cards), 3):
        suits[cards[i]] += 1
    for i in ['P', 'K', 'H', 'T']:
        print(13 - suits[i])

if __name__ == '__main__':
    main()
