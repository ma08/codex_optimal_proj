

def main():
    """
    Main function
    """
    n, k = list(map(int, input().split()))
    s = list(input())
    available_chars = set(input().split())
    count = 0
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            if set(s[j:j+i]).issubset(available_chars):
                count += 1
    print(count)

if __name__ == "__main__":
    main()
