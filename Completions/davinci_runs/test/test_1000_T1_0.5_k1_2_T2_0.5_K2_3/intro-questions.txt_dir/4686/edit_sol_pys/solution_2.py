

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def main():
    n = int(input())
    print(get_divisors(n))

if __name__ == '__main__':
    main()
