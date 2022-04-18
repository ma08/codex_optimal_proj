
from collections import Counter

def main():
    n = int(input())
    socks = [int(i) for i in input().split()]
    socks_dict = Counter(socks)
    print(sum([socks_dict[key] // 2 for key in socks_dict]))

if __name__ == "__main__":
    main()
