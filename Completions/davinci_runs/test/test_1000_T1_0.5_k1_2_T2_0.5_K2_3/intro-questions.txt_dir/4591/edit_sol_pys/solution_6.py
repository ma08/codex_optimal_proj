

def main():
    # Read input
    N = int(input())
    S = input()

    # Count the number of vowels
    vowels = 0
    for char in S:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1

    # Print the number of vowels
    print(vowels)

if __name__ == "__main__":
    main()
