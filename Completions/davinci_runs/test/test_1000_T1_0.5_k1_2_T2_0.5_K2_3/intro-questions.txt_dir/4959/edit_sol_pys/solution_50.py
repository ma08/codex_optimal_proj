

def main():
    e, f, c = map(int, input().split())
    # e is empty bottles, f is full bottles, c is cost of one bottle
    count = 0
    while e + f >= c:
        # while the number of empty bottles plus full bottles is greater than or equal to the cost of one bottle
        count += (e + f) // c
        e, f = (e + f) % c, e // c
    print(count)

if __name__ == '__main__':
    main()
