

def main():
    """
    1. Get input
    2. Loop through the input
    3. If first letter is not equal to second letter, add it to final count
    4. Otherwise, continue
    5. Loop until you reach end of input
    """
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        if s[i] != s[i+1]:
            count += 1
        else:
            continue
    print(count)

if __name__ == "__main__":
    main()
