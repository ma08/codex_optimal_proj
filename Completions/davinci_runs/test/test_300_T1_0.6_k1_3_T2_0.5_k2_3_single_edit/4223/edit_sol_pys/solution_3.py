

def main():
    """
    1. Get input
    2. If first letter is not equal to second letter, add it to final count
    3. Otherwise, continue
    4. Loop until you reach end of input
    """
    n = int(input())
    s = input()
    count = 0
    for i in range(n-1):
        if s[i] != s[i+1]:
            count += 1
        else:
            continue
    print(count)

if __name__ == "__main__":
    main()
