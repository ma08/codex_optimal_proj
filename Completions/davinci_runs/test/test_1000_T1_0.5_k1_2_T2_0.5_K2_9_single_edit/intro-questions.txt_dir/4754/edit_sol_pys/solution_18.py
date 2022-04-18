

from collections import Counter

def main():
    n = int(input())
    socks = [int(i) for i in input().split()]
    if len(socks) % 2 == 1 or len([i for i in socks_dict if socks_dict[i] % 2 == 1]) > 0:
        return print("impossible")
    socks_dict = Counter(socks)
    moves = 0
    while len(socks_dict) > 0:
        socks_dict = Counter({key: socks_dict[key] - 2 for key in socks_dict if socks_dict[key] >= 2})
        moves += 1
    return print(moves * 2)

if __name__ == "__main__":
    main()
