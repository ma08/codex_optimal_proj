

def main():
    a, b, c = [int(x) for x in input().split()]
    print("Yes" if a + b >= c else "No")

if __name__ == '__main__':
    main()
