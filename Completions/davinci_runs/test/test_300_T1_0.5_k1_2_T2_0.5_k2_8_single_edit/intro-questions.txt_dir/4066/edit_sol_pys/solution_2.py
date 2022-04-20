

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_lcm = lcm(a[0], a[1])
    min_i = 1
    min_j = 2
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if lcm(a[i], a[j]) < min_lcm:
                min_lcm = lcm(a[i], a[j])
                min_i = i + 1
                min_j = j + 1
    print(min_i, min_j)

if __name__ == '__main__':
    main()
