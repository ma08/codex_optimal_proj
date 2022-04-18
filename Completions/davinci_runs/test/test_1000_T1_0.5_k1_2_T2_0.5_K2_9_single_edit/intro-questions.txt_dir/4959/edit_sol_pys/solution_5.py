


def main():
    a, b = map(int, input().split())
    count = 0
    while a <= b:
        a *= 3
        b *= 2
        count += 1
    print(count)

if __name__ == '__main__':
    main()

def main():
    e, f, c = map(int, input().split())
    count = 0
    while e + f >= c:
        count += (e + f) // c
        e, f = (e + f) % c, e // c
    print(count)

if __name__ == '__main__':
    main()
