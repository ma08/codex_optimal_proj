

def main():
    n = int(input())  # number of people
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    l = [a, b, c, d, e]  # list of people
    l.sort()  # sort by ascending order

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
