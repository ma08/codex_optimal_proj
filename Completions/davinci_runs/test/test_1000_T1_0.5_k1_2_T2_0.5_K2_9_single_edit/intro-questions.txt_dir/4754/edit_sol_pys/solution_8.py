

from collections import Counter

def main():
    n = int(input())
    socks = [int(i) for i in input().split()]
    socks_dict = Counter(socks)
    print(sum(socks_dict.values()) // 2)

if __name__ == "__main__":
    main()
