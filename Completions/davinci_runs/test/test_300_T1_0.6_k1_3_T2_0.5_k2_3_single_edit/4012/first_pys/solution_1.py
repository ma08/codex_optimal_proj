

def main():
    """
    If a divides b, then we can choose b = a * k and then c = b * k'.
    If b divides c, then we can choose c = b * k and then a = c * k'.
    Thus, we can choose a = 1 and then b = 1 * k and c = b * k'.
    """
    t = int(input())
    for _ in range(t):
        a, b, c = [int(x) for x in input().split()]
        k = b // a
        k_ = c // b
        print(k + k_)
        print(1, a * k, b * k_)


if __name__ == "__main__":
    main()