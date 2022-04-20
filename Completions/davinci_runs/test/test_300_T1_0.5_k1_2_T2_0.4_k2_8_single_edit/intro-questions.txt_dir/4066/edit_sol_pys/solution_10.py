
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_lcm = lcm(a[0], a[1])  # min lcm
    min_i = 1  # min i
    min_j = 2  # min j
    for i in range(len(a)):  # loop through array
        for j in range(i + 1, len(a)):  # loop through array
            if lcm(a[i], a[j]) < min_lcm:  # if lcm is less than min lcm
                min_lcm = lcm(a[i], a[j])  # update min lcm
                min_i = i + 1  # update min i
                min_j = j + 1  # update min j
    print(min_i, min_j)  # print min i and min j

if __name__ == '__main__':
    main()
