import math

def main():
    b, k, g = [int(x) for x in input().split()]
    print(math.ceil(b/k/g))

if __name__ == "__main__":
    main()
