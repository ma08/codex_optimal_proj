
import math

def main():
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(math.ceil(a/b))

if __name__ == "__main__":
    main()
