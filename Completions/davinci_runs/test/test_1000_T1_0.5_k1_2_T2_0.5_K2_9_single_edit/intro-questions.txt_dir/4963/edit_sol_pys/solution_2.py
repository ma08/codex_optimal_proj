import math

n = int(input())

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    divisors = get_divisors(sum(a))
    ans = 0
    for divisor in divisors:
        count = 0
        for i in range(n):
            count += math.ceil(a[i] / divisor)
        if count <= k:
            ans = divisor
            break
    print(ans)

if __name__ == '__main__':
    main()
d = list(map(int, input().split()))

lineup = [0] * n

for i in range(1, n):
    lineup[d[i-1]] = i

print(*lineup)
