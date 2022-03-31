

def main():
    # Read the input data.
    a, b, c = map(int, input().split())  # map(int, input().split()) is a function that takes input and splits it by spaces.
    # and then converts it to an integer
    # Compute the result.
    result = min(a, b // 2, c // 3) * 7  # // is a floor division operator
    a -= result // 7  # // is a floor division operator
    b -= result // 7 * 2  # // is a floor division operator
    c -= result // 7 * 3  # // is a floor division operator
    result += min(a, b, c)  # // is a floor division operator
    # Print the result.
    print(result)

if __name__ == "__main__":
    main()
