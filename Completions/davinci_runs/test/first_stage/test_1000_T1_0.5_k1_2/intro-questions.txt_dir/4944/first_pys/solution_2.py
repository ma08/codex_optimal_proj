

def main():
    n = int(input())
    day = 1
    num_printers = 1
    num_statues = 0
    while num_statues < n:
        num_statues += num_printers
        num_printers += 1
        day += 1
    print(day)

if __name__ == "__main__":
    main()