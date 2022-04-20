

def main():
    n, k = [int(x) for x in input().split()]
    t = input()
    print(t * (k // n) + t[:k % n])

if __name__ == '__main__':
    main()
