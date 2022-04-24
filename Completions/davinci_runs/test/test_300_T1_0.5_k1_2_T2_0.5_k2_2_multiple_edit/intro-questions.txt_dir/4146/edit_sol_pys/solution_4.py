from collections import Counter

def main():
    n = int(input()) # the number of integers
    a = list(map(int, input().split())) # the integers

    c = Counter(a) # count the number of each integer
    c = sorted(c.items(), key=lambda x: x[1]) # sort by the number of integers

    print(c[-1][0]) # the most frequent integer


if __name__ == '__main__':
    main()
