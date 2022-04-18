def main():
    n = int(input())
    d = list(map(int, input().split()))

    cleaning = 0
    dirty = 0
    for i in range(n):
        while dirty >= 20:
            cleaning += 1
            dirty -= 20
        dirty += (d[i] - 1)

    while dirty >= 20:
        cleaning += 1
        dirty -= 20

    print(cleaning)

if __name__ == '__main__':
    main()
