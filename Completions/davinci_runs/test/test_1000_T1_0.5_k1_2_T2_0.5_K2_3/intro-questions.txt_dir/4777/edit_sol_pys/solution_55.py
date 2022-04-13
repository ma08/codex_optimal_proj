
import sys

def main(k):
    a, b = 1, 1
    for _ in range(k):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    k = int(sys.stdin.readline())
    a = main(k)
    print(a)
