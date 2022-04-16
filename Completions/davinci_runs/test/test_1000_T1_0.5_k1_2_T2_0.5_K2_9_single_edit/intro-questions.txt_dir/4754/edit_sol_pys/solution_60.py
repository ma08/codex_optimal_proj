

from collections import Counter

def main():
    n = int(input())
    socks = [int(i) for i in input().split()]
    if n % 2 == 1:
        print("impossible")
        return
    socks_dict = Counter(socks)
    moves = 0
    while len(socks_dict) > 0:
        # print(socks_dict)
        socks_dict = Counter({key: socks_dict[key] - 2 for key in socks_dict if socks_dict[key] >= 2})
        moves += 1
    print(moves)

if __name__ == "__main__":
    main()
