

def main():
    """
    This function is the main function.
    """
    n = int(input())
    result = 0
    for i in range(1, n // 2 + 1):
        if (n-i) % i == 0:
            result += 1
    print(result + 1)

# The following is the standard boilerplate that calls the main() function.

if __name__ == "__main__":
    main()
