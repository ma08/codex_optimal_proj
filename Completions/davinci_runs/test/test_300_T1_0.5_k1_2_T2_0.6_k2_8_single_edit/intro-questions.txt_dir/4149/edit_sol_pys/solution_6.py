

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n, b):
    a = []
    for i, val in enumerate(b):
        if i % 2 == 0:
            a.append(val)
        else:
            if is_prime(val):
                a.append(val)
            else:
                a.append(val + 1)
    return a

def main():
    n = int(input())
    b = [int(i) for i in input().split(' ')]
    a = solve(n, b)
    print(' '.join([str(i) for i in a]))

if __name__ == '__main__':
    main()
