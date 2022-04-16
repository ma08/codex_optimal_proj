

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    t = int(input())

    if t ** 2 == (a - c) ** 2 + (b - d) ** 2:
        print("Y")
    else:
        print("N")

main()
