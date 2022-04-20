

def input():
    return int(input())

def input_list():
    return list(map(int, input().split()))

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

def main():
    N = input()
    A = input_list()
    print(max(gcd(a, b) for a in A for b in A))

if __name__ == '__main__':
    main()