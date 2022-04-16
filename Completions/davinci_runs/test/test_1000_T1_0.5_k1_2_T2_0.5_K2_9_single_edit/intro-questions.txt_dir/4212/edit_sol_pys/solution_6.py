from collections import defaultdict

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def main():
    n = int(input())
    for i in range(1, n+1):
        divisors = make_divisors(i)
        print(divisors)

if __name__ == '__main__':
    main()
