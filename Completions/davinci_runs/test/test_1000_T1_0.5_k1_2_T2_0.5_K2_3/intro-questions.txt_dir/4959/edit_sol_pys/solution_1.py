
def main():
    e, f, c = map(int, input().split())  # input
    n = (e + f) // c  # number of empty bottles
    left = (e + f) % c  # number of bottlecaps left
    while n + left >= c:  # while there are enough bottlecaps to buy a new bottle
        n += left // c  # buy a new bottle
        left = (left % c) + (left // c)  # bottlecaps left after buying a new bottle
    print(n)  # print number of empty bottles

if __name__ == '__main__':
    main()
