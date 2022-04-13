

def main():
    """main function"""
    input_number = int(input())
    k = 0
    while input_number > 1:
        k += 1
        input_number = input_number // (2 * k + 1)
    print(k)

if __name__ == "__main__":
    main()
