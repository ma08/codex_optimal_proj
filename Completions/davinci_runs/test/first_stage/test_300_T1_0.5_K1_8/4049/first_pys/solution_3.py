

def main():
    """
    This is the main function.
    """
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(calculate_min(a, b), calculate_max(a, b))

def calculate_min(a, b):
    """
    Calculate the minimum number of rounds Alice can win.
    """
    return min(a[2], b[0]) + min(a[1], b[2]) + min(a[0], b[1])

def calculate_max(a, b):
    """
    Calculate the maximum number of rounds Alice can win.
    """
    return max(a[2], b[0]) + max(a[1], b[2]) + max(a[0], b[1])

if __name__ == "__main__":
    main()