

def main():
    n, k = [int(x) for x in input().split()]
    t = input()
    s = t
    while len(s) < k * n:
        s += t
    print(s[:k * n])

if __name__ == '__main__':
    main()