

def max_triple(x,y,z):
    if x == y and y == z:
        return "YES\n{} {} {}".format(x,y,z)
    elif x == y or x == z or y == z:
        return "NO"
    elif x > y and x > z:
        return "YES\n{} {} {}".format(x, max(y,z), min(y,z))
    elif y > x and y > z:
        return "YES\n{} {} {}".format(y, max(x,z), min(x,z))
    elif z > x and z > y:
        return "YES\n{} {} {}".format(z, max(x,y), min(x,y))

def main():
    t = int(input())
    for _ in range(t):
        x,y,z = map(int,input().split())
        print(max_triple(x,y,z))

if __name__ == "__main__":
    main()
