

def read_input():
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    offers = []
    for i in range(m):
        x, y, w = map(int, raw_input().split())
        offers.append((x, y, w))
    return n, m, a, offers

def solve(n, m, a, offers):
    pass

def main():
    n, m, a, offers = read_input()
    print solve(n, m, a, offers)

if __name__ == "__main__":
    main()