import math

def main():
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))

if __name__ == "__main__":
    main()
