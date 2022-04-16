import collections

def main():
    n = int(input())
    cheeses = collections.defaultdict(int)
    for i in range(n):
        cheese = input().split()
        cheeses[cheese[1]] += 1
    print(min(cheeses.values()))

if __name__ == "__main__":
    main()
