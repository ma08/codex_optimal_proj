from itertools import permutations

if __name__ == '__main__':
    s, n = input().split()
    for p in permutations(sorted(s), int(n)):
        print(''.join(p))
