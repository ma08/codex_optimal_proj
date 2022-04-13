

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n != 1

def main():
    n = int(input())
    print("Yes" if is_prime(n) else "No")

if __name__ == "__main__":
    main()
