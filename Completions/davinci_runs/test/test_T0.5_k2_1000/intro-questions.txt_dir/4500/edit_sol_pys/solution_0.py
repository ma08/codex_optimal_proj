

def main():
    a, b = [int(x) for x in input().split()]
    print("Yes" if a + b >= 10 else "No")

if __name__ == '__main__':
    main()
