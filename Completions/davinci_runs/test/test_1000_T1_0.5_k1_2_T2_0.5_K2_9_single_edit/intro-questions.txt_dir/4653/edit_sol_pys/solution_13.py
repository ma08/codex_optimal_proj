
import sys

def main():
    """
    Main Function
    """
    num_cases = int(sys.stdin.readline().strip())
    for _ in range(num_cases):  # pylint: disable=unused-variable
        n, k = [int(x) for x in sys.stdin.readline().split()]
        if n < k:
            print(n)
        else:
            print((n // k) * k + min(k // 2, n % k))

if __name__ == "__main__":
    main()
