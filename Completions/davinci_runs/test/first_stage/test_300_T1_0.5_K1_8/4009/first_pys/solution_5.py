

def main():
    n, x, y = map(int, input().split())
    number = input()
    remainder = int(number[-y:])
    mod = 10**x
    if remainder == 0:
        print(0)
    else:
        print(mod - remainder)

if __name__ == "__main__":
    main()