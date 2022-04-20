

import math

def main():
    a, b, c = map(int, input().split())
    s = (a + b + c) / 2
    print(math.sqrt(s * (s - a) * (s - b) * (s - c)))

if __name__ == "__main__":
    main()
