

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        divisors = [int(x) for x in input().split()]
        x = find_x(n, divisors)
        print(x)

def find_x(n, divisors):
    if n == 1:
        return divisors[0] * 2
    if n == 2:
        return divisors[0] * divisors[1]
    return -1

if __name__ == "__main__":
    main()