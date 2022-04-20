

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    lcm_list = []
    for i in range(n):
        for j in range(i + 1, n):
            lcm_list.append(lcm(a[i], a[j]))
    print(lcm_list.index(min(lcm_list)) + 1, lcm_list.index(min(lcm_list)) + 2)

if __name__ == '__main__':
    main()
