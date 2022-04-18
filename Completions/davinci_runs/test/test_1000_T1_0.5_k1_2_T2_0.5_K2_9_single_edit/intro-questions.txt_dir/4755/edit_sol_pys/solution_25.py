
import sys

def main():
    # Get the inputs
    C, K = [int(x) for x in sys.stdin.readline().split()]  # noqa
    
    # Round to nearest 10^K
    C = C // (10**K) * (10**K)  # noqa
    if C != 0:
        C += 10**K  # noqa
    print(C)

if __name__ == "__main__":
    main()
