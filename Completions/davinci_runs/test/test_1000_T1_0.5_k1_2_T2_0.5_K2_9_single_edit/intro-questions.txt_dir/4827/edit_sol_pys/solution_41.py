
def main():
    # Read the number of words
    N = int(input())

    # Read the words and calculate the number of letters
    number_of_letters = sum(len(input()) for i in range(N))
    print(number_of_letters)

if __name__ == "__main__":
    main()
