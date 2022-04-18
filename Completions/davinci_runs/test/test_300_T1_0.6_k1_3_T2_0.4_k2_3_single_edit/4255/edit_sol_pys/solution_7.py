
import math

def main():
    a, b, c, d = input().split()
    a, b, c, d = int(a), int(b), int(c), int(d)
    print(math.sqrt((a - c) ** 2 + (b - d) ** 2))

if __name__ == "__main__":
    main()
