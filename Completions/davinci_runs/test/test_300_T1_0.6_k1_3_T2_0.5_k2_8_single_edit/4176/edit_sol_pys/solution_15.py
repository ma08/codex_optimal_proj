
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    a, b = [int(i) for i in input().split()]
    print(lcm(a, b))
