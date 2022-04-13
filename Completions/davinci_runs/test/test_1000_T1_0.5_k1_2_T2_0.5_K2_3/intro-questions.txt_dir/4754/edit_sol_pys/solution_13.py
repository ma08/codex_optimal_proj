

from collections import Counter

def main():
    n = int(input())
    socks = [int(i) for i in input().split()]
    if len(socks) % 2 == 1:
        print("impossible")
        return
    socks_dict = Counter(socks)  # dict of socks and their counts
    moves = 0  # number of moves
    while len(socks_dict) > 0:
        # print(socks_dict)
        socks_dict = Counter({key: socks_dict[key] - 2 for key in socks_dict if socks_dict[key] >= 2})  # remove 2 socks from the dict
        moves += 1
    print(moves * 2)

if __name__ == "__main__":
    main()
