
def main():
    d, k = [int(x) for x in input().split()]
    if d == 1:
        print("1 {}".format(k + 1))
    elif d == 2:
        print("1 2")
        print("2 {}".format(k + 1))
    elif d == 3:
        print("1 2")
        print("2 3")
        print("3 {}".format(k + 1))
    else:
        print("1 2")
        print("2 3")
        print("1 4")
        print("4 {}".format(k + 1))

if __name__ == '__main__':
    main()
