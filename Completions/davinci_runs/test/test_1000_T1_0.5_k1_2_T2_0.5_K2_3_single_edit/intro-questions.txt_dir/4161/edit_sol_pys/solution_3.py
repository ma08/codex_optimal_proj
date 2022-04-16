
import sys

K = int(sys.stdin.readline())

def main():
    print(sum([1 for a in range(1, K+1) for b in range(1, K+1) for c in range(1, K+1) if a * a + b * b == c * c]))

main()
