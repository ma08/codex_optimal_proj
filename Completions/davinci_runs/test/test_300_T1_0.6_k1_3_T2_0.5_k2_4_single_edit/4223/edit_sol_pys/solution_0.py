

def main():
    """
    1. Get input
    2. Loop until you reach end of input
        2.1 If first letter is not equal to second letter, add it to final count
        2.2 Otherwise, continue
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
