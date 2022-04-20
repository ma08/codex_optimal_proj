import math

def divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def main():
    N = int(input())

    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()



N = int(input())
print(N)
