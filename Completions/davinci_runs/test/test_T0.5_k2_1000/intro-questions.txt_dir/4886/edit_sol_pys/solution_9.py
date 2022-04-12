
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    n, k = [int(x) for x in input().split()]
    if k == 0:
        print("Your wish is granted")
    elif k == 1:
        print("You will become a flying monkey")
    elif n % 2 == 0:
        print("Your wish is granted")
    elif n == 3:
        print("You will become a flying monkey")
    elif n == 5:
        print("You will become a flying monkey")
    elif n == 7:
        print("You will become a flying monkey")
    elif n > 7 and is_prime(n):
        print("You will become a flying monkey")
    else:
        print("Your wish is granted")

if __name__ == "__main__":
    main()
