import math

def main():
    v = int(input())
    if v == 1:
        print(6)
    elif v == 2:
        print(12)
    elif v == 3:
        print(14)
    else:
        a = math.ceil(math.sqrt(v))
        b = math.floor(v / a)
        if a * b < v:
            b += 1
        print(2 * (a + b))

if __name__ == "__main__":
    main()
