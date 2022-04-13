
import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    if d % 2 == 1 or d < a or d < b or d < c or d > a + b + c * 2:
        print("impossible")
        return
    for i in range(0, d // a + 1):
        for j in range(0, d // b + 1):
            for k in range(0, d // c + 1):
                if i * a + j * b + k * c == d:
                    print(i, j, k)

if __name__ == "__main__":
    main()
