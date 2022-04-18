

def main():
    """
    Main function
    """
    n, k = list(map(int, input().split()))
    s = list(input())
    available_chars = set(input().split())
    s_set = set(s)
    #print(s_set)
    #print(available_chars)
    count = 1
    for i in range(1, n+1):
        for j in range(0, n-i):
            if s_set.issubset(available_chars):
                count += 1
            s_set.remove(s[j+i])
    print(count)

if __name__ == "__main__":
    main()
