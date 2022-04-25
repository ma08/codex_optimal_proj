'''
from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] for card in cards[:K])

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
'''

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n != 1

def main():
    N = int(input())
    if is_prime(N):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
