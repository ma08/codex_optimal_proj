
from math import sqrt

def main():
    n = int(input())
    rods = [0.0]
    for _ in range(n):
        a, b, c = [int(x) for x in input().split()]
        rods.append(rods[-1] + a + b - sqrt(a*a + b*b - c*c))
    ans = 0.0
    for i in range(1, n + 1):
        ans = max(ans, rods[i])
    print(ans)

if __name__ == "__main__":
    main()
