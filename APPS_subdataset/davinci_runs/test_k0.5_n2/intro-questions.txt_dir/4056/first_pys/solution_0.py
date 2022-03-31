


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    lcm_arr = arr[0]
    for i in range(1, n):
        lcm_arr = lcm(lcm_arr, arr[i])
    print(len(str(lcm_arr)))


if __name__ == '__main__':
    main()