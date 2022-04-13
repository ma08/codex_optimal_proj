

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def LCM(a, b):

    return (a * b) // GCD(a, b)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_lcm = LCM(a[0], a[1])
    min_i = 1
    min_j = 2
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if LCM(a[i], a[j]) < min_lcm:
                min_lcm = LCM(a[i], a[j])
                min_i = i + 1
                min_j = j + 1
    print(min_i, min_j)

if __name__ == '__main__':
    main()
