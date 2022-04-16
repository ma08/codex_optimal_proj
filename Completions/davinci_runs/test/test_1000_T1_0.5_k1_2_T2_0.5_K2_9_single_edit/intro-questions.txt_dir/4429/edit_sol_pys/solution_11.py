


def max_triple(x, y, z):
    if x == y:
        if y == z:
            return "YES\n{} {} {}".format(x, y, z)
        else:
            return "NO"
    elif x == z:
        return "NO"
    elif y == z:
        return "NO"
    elif (x > y) and (x > z):
        if y > z:
            return "YES\n{} {} {}".format(x, y, z)
        else:
            return "YES\n{} {} {}".format(x, z, y)
    elif (y > x) and (y > z):
        if x > z:
            return "YES\n{} {} {}".format(y, x, z)
        else:
            return "YES\n{} {} {}".format(y, z, x)
    elif (z > x) and (z > y):
        if x > y:
            return "YES\n{} {} {}".format(z, x, y)
        else:
            return "YES\n{} {} {}".format(z, y, x)


def main():
    t = int(input())
    for _ in range(t):
        x, y, z = map(int, input().split())
        print(max_triple(x, y, z))


if __name__ == "__main__":
    main()
