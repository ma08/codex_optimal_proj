
import sys

def main(k):  # fibonacci
    a, b = 1, 0
    for _ in range(k):
        a, b = b, a + b
    return a, b

if __name__ == "__main__":
    k = int(sys.stdin.readline())
    a, b = main(k)
    print(a, b)
