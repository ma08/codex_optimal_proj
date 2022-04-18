

def max_triple(x, y, z):
    if x == y == z:
        return "YES\n{} {} {}".format(x, y, z)
    if x == y or x == z or y == z:
        return "NO"
    if (x > y) and (x > z):
        if y > z: return "YES\n{} {} {}".format(x, y, z)
        else: return "YES\n{} {} {}".format(x, z, y)
    if (y > x) and (y > z):
        if x > z: return "YES\n{} {} {}".format(y, x, z)
        else: return "YES\n{} {} {}".format(y, z, x)
    if (z > x) and (z > y):
        if x > y: return "YES\n{} {} {}".format(z, x, y)
        else: return "YES\n{} {} {}".format(z, y, x)

def main():
    t = int(input())
    for _ in range(t):
        x, y, z = map(int, input().split())
        print(max_triple(x, y, z))

if __name__ == "__main__":
    main()
