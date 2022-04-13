from math import ceil, floor, sqrt

def main():
    V = int(input())
    if V == 1:
        print(6)
    elif V == 2:
        print(12)
    elif V == 3:
        print(14)
    else:
        a = ceil(sqrt(V))
        b = floor(V / a)
        if a * b < V:
            b += 1
        print(2 * (a + b))

if __name__ == "__main__":
    main()
