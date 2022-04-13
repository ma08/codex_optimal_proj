from math import sqrt

def main():
    n = int(input())
    rods = []
    for _ in range(n):
        a, b, c = [int(x) for x in input().split()]
        rods.append((a, b, c))
    rods.sort(key=lambda x: x[0] + x[1])
    rods.reverse()
    ans = 0
    for a, b, c in rods:
        if ans == 0:
            ans = a + b - sqrt(a * a + b * b - c * c)
        else:
            ans = max(ans, ans + a + b - sqrt(a * a + b * b - c * c))
    print(ans)

if __name__ == "__main__":
    main()
