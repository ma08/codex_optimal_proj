
def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_sort = [''.join(sorted(s)) for s in S]
    print(sum([c * (c-1) // 2 for c in collections.Counter(S_sort).values()]))

if __name__ == '__main__':
    main()
