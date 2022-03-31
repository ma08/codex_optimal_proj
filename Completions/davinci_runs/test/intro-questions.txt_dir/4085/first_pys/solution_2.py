

t = int(input())

for _ in range(t):
    n = int(input())
    divisors = list(map(int, input().split()))
    divisors.sort(reverse=True)

    for i in range(len(divisors) - 1):
        if divisors[i] % divisors[i + 1] != 0:
            print(-1)
            break
    else:
        print(divisors[0] + divisors[-1])