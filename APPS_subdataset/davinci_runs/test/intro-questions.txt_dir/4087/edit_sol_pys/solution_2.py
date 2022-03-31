

def sum_of_digits(m):
    s = 0
    while m:
        s += m % 10
        m //= 10
    return s

def is_interesting(m):
    return sum_of_digits(m) % 4 == 0

def next_interesting(m):
    while not is_interesting(m):
        m += 1
    return m

if __name__ == "__main__":
    m = int(input())
    print(next_interesting(m))
