
def main():
    n = int(input())
    day = 1
    num_printers = 1
    num_statues = 1
    while num_statues < n:
        if num_statues % 2 == 0:
            num_printers += 1
        day += 1 
        num_statues += num_printers 
    print(day)

if __name__ == "__main__":
    main()
