
def main():
    a, b = [int(x) for x in input().split()]
    print(a if int(str(a)[::-1]) > int(str(b)[::-1]) else b)


main()
