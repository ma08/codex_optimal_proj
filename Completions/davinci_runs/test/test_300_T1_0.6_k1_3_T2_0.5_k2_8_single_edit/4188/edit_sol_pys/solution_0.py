
# ----- Solution -----
def main():
    n = int(input())

    if n % 2 == 1:
        print(0)
    else:
        print(int(2 ** (n / 2)))

# ----- Main -----
main()
