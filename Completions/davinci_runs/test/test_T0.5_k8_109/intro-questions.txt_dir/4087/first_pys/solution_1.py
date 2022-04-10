

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_interesting(n):
    return sum_of_digits(n) % 4 == 0

def next_interesting(n):
    while not is_interesting(n):
        n += 1
    return n

def main():
    a = int(input())
    print(next_interesting(a))

if __name__ == "__main__":
    main()