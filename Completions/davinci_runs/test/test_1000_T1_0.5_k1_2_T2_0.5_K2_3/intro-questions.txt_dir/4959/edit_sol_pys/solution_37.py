
def main():
    e, f, c = map(int, input().split())
    count = 0
    while e + f >= c:
        count += (e + f) // c
        e, f = (e + f) % c, e // c
    print(count)


if __name__ == '__main__':
    main()
