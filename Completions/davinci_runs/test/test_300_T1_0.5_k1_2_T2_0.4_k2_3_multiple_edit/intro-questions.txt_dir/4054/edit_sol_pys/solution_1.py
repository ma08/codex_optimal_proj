

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a = [int(x) for x in input().split()]  # input the list of numbers
    b = a[0]  # assign the first number to b
    for i in range(1, len(a)):  # iterate through the list of numbers
        b = lcm(b, a[i])  # assign the lcm of b and a[i] to b
    print(b)  # print the lcm of the list of numbers

if __name__ == '__main__':
    main()
