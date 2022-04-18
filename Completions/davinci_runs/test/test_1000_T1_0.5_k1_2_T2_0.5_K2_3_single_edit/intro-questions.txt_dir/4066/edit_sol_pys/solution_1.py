

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_lcm = float('inf')
    min_i = -1
    min_j = -1
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if lcm(a[i], a[j]) < min_lcm:
                min_lcm = lcm(a[i], a[j])
                min_i = i + 1
                min_j = j + 1
    if min_i == -1 or min_j == -1:
        print(1, 2)
    else:
        print(min_i, min_j)

if __name__ == '__main__':
    main()
