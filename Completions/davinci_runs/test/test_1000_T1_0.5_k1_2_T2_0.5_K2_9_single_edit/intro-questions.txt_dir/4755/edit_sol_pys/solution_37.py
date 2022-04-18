
import sys

def main():
    # Get the inputs
    C, K = [int(x) for x in sys.stdin.readline().split()]

    # Round to nearest 10^K
    C = C // (10 ** K) * (10 ** K)
    if C != 0:
        C += 10 ** K
    print(C)

if __name__ == "__main__":
    main()
