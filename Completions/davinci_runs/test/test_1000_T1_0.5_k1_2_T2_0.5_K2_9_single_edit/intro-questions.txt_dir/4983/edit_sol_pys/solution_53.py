

def main():
    x = int(input())
    while x > 9:
        digits = [int(d) for d in str(x)]  # list comprehension
        product = 1
        for d in digits:
            if d != 0:
                product *= d
        x = product
    print(x)

if __name__ == "__main__":
    main()
