

def main():
    n = int(input())
    day = 1
    printer = 1
    statue = 0
    while statue < n:
        statue += printer
        printer += 1
        day += 1
    print(day)

if __name__ == "__main__":
    main()
