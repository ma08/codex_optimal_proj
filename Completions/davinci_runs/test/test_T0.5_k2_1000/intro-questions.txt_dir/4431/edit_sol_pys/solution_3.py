

def main():
    """
    Main function
    """
    n, k = list(map(int, input().split()))
    s = list(input())
    available_chars = set(input().split())
    s_set = set(s)
    count = 0
    for i in range(0, n):
        if s_set.issubset(available_chars):
            count += 1
        s_set.remove(s[i])
    print(count)

if __name__ == "__main__":
    main()
