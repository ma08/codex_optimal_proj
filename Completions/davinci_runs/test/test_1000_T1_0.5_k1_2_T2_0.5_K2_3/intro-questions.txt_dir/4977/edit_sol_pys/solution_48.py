
def main():
    a, b, c, d, t = map(int, input().split()) # a,b,c,d,tをint型で入力

    if (a - c) ** 2 + (b - d) ** 2 == t ** 2:
        print("Y")
    else:
        print("N")

main()
