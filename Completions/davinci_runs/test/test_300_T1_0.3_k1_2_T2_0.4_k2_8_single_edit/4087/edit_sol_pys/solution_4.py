

def sum_of_digits(n):
    return sum(int(i) for i in str(n)) % 4 == 0

def next_multiple(n):
    while not sum_of_digits(n):
        n += 1
    return n

def main():
    n = int(input())
    print(next_multiple(n))

if __name__ == "__main__":
    main()
