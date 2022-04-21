

def main():
    n = int(input())
    m = int(input())
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    i = 0
    while m > 0:
        m -= numbers[i]
        i += 1
    print(i)


if __name__ == "__main__":
    main()
