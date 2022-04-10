

def main():
    n = int(input())
    for _ in range(n):
        a, b = [int(x) for x in input().split()]
        if a == b:
            print(0)
        elif a < b:
            if (b - a) % 2 == 0:
                print(2)
            else:
                print(1)
        else:
            if (a - b) % 2 == 0:
                print(1)
            else:
                print(2)


main()
