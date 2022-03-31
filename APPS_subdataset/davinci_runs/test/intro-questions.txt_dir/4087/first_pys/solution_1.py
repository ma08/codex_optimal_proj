

def sum_of_digits(n):
    s = 0
    while n:
        s += n%10
        n //= 10
    return s

def is_interesting(n):
    return sum_of_digits(n) % 4 == 0

def next_interesting(n):
    while not is_interesting(n):
        n += 1
    return n

if __name__ == "__main__":
    n = int(input())
    print(next_interesting(n))