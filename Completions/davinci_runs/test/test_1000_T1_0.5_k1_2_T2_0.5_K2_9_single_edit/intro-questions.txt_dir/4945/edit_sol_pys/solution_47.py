

def solve(n, k, c):
    l = []
    while n > 0:
        l.append(n % k)
        n /= k
    l.reverse()
    return l

def main():
    n, k, c = [int(x) for x in raw_input().split()]
    l = solve(n, k, c)
    print " ".join(map(str, l))

if __name__ == '__main__':
    main()
