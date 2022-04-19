

def sum_of_digits(n):
    return sum(int(i) for i in str(n)) % 4 == 0

def next_interesting(n, i=1):
    while not sum_of_digits(n):
        n += i
        i += 1
    return n - i + 1

def main():
    n = int(input())
    print(next_interesting(n))

if __name__ == "__main__":
    main()
