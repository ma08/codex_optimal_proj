

def main():
    n = int(input())
    day = 1
    num_printer = 1
    num_statue = 0
    while num_statue < n:
        num_statue += num_printer
        num_printer += 1
        day += 1
    print(day)

if __name__ == "__main__":
    main()
