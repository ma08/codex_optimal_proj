

def main():
    a, b, k = map(int, input().split())
    divisors = sorted(set(divisor(a) + divisor(b)))
    print(divisors[-k])

def divisor(num):
    i = 1
    divisors = []
    while i * i <= num:
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num//i)
        i += 1
    return divisors

if __name__ == '__main__':
    main()