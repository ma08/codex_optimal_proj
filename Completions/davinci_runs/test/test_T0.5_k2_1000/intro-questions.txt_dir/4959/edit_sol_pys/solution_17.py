

def main():
    e, f, c = map(int, input().split())  # e: empty, f: full, c: capacity
    empty = (e + f) // c  # empty: empty bottles
    left = (e + f) % c  # left: left over
    while empty + left >= c:  # while there are enough to exchange
        empty += left // c  # exchange all the left over
        left = (left % c) + (left // c)  # calculate the left over
    print(empty)  # print the total number of empty bottles

if __name__ == '__main__':
    main()
