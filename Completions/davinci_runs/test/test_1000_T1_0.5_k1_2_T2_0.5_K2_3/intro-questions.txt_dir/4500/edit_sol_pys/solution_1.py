

def main():
    a, b, c, d = [int(x) for x in input().split()]
    print("Yes") if a + b >= c + d else print("No")

if __name__ == '__main__':
    main()
