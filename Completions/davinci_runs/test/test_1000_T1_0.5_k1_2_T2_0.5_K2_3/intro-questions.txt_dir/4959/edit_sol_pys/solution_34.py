
def main():
    e, f, c = map(int, input().split())  # e = empty bottles, f = full bottles, c = caps per bottle
    n = (e + f) // c  # n = number of full bottles
    left = (e + f) % c  # left = number of empty bottles
    while n + left >= c:  # if there are enough bottles to exchange
        n += left // c  # exchange empty bottles for full bottles
        left = (left % c) + (left // c)  # calculate the remaining empty bottles
    print(n)

if __name__ == '__main__':
    main()
