

def main():
    x, y = map(int, input().split())
    a, b = map(int, input().split()) 

    print("{} {}".format(x - b, y + a))
    print("{} {}".format(x - a, y - b))
    print("{} {}".format(x + b, y - a))
    print("{} {}".format(x + a, y + b))

main()
