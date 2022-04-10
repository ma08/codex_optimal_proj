

def main():
    # Read the input data.
    a, b, c = map(int, input().split())
    # Compute the result.
    result = min(a, b // 2, c // 3) * 7
    a -= result // 7
    b -= result // 7 * 2
    c -= result // 7 * 3
    result += min(a, b, c)
    # Print the result.
    print(result)

if __name__ == "__main__":
    main()