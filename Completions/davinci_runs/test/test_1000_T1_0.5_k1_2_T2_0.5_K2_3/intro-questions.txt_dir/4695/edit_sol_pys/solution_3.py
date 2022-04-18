
def main(x, y, z):
    if (x == y and y == z) or (x == y and y == z):
        return "yes"
    else:
        return "no"

if __name__ == "__main__":
    x, y = map(int, input().split())
    z = int(input())
    print(main(x, y, z))
