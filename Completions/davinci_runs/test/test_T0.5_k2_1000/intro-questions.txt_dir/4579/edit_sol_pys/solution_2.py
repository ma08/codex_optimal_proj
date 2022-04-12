
import sys

def main():
    # Read the input
    N = int(input())
    items = [input() for _ in range(N)]

    # Solve
    result = len(set(items))

    # Output the result
    print(result)

if __name__ == "__main__":
    main()
