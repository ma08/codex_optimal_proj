

def main():
    """
    1. Get input
    2. If first letter is not equal to second letter, add it to final count
    3. Otherwise, continue
    4. Loop until you reach end of input
    """
    n = int(input())
    s = input()
    if n == 1:
        print(0)
        return
    count = 0
    for i in range(n):
        if i == n-1:
            break
        if s[i] != s[i+1] and i != n-1:
            count += 1
        else:
            continue
    print(count)

if __name__ == "__main__":
    main()
