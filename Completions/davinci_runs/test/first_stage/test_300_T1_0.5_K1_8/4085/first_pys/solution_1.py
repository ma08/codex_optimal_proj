

t = int(input())
for i in range(t):
    n = int(input())
    divisors = list(map(int, input().split()))
    divisors.sort()
    if n == 1:
        print(divisors[0] * 2)
    else:
        x = divisors[0] * divisors[1]
        for j in range(2, len(divisors)):
            if divisors[j] * divisors[j - 1] != x:
                print(-1)
                break
        else:
            print(x)