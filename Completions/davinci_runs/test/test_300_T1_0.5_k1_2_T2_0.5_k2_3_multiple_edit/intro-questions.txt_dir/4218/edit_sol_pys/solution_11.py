
def main():
    n = int(input()) # number of people
    m = int(input()) # number of pairs
    pairs = [list(map(int, input().split())) for _ in range(m)]
    print(pairs)

if __name__ == '__main__':
    main()
