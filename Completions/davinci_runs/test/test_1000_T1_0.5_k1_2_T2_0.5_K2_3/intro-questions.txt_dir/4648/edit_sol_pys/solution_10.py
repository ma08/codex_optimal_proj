
def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        moves = 0
        while n > 1:
            if n % 3 == 0:
                n /= 3
                moves += 2
            else:
                n *= 2
                moves += 2
        print("Case %d: %d" % (i, moves))

if __name__ == "__main__":
    main()
