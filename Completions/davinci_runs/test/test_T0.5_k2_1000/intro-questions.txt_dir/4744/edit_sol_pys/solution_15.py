import math


def main():
    V = int(input())
    if V == 1:
        print(5)
    elif V == 2:
        print(11)
    elif V == 3:
        print(13)
    else:
        a = math.ceil(math.sqrt(V))
        b = math.floor(V / a)
        if a * b < V:
            b += 1
        print(2 * (a + b))

if __name__ == "__main__":
    main()
