
def main():
    e, f, c = map(int, input().split())  # e: empty bottles, f: full bottles, c: empty bottles exchanged for 1 full bottle
    count = 0
    while e + f >= c:  # when e + f < c, the number of full bottles will not increase anymore
        count += (e + f) // c
        e, f = (e + f) % c, e // c  # update e, f
    print(count)

if __name__ == '__main__':
    main()
