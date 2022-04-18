

def main():
    n = int(input())
    day = 1
    printer = 1
    statues = 0
    while statues < n:
        statues += printer
        printer += 1
        day += 1
    print(day)

if __name__ == "__main__":
    main()
