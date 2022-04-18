

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input())
    if is_prime(n):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
