

def sum_of_digits(n):
    return sum(int(i) for i in str(n) if i != '-')

def is_interesting(n):
    return sum_of_digits(n) % 4 == 0 or n % 4 == 0

def next_interesting(n):
    while not is_interesting(n):
        n += 1
    return n

def main():
    n = int(input())
    print(next_interesting(n))

if __name__ == "__main__":
    main()
