

import math

def main():
    V = int(input())
    if V == 1:
        print(6)
    elif V == 2:
        print(12)
    elif V == 3:
        print(14)
    else:
        a = math.ceil(math.sqrt(V))  # ширина
        b = math.floor(V / a)  # высотаa
        if a * b < V:
            b += 1
        print(2 * (a + b))

if __name__ == "__main__":
    main()
