

def getDivisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def main():
    n = int(input())
    d = list(map(int, input().split()))
    divisors = set(d)
    for i in divisors:
        if d.count(i) > 1:
            d.remove(i)
    d.sort()
    x = d[-1]
    y = d[-1]
    for i in range(len(d)-2, -1, -1):
        if d[i] in getDivisors(x):
            x *= d[i]
        else:
            y *= d[i]
    print(x, y)

main()