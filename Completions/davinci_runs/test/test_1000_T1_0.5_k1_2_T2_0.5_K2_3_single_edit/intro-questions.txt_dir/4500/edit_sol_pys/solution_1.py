

def main():
    a, b = [int(x) for x in input().split()]
    print("a < b" if a < b else "a >= b")

if __name__ == '__main__':
    main()
