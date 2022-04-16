

def main():
    """
    Main function
    """
    n, k = list(map(int, input().split()))
    s = list(input())
    available_chars = set(input())
    s_set = set(s[:k])
    #print(s_set)
    #print(available_chars)
    count = 0
    for i in range(0, n-k+1):
            if s_set.issubset(available_chars):
                count += 1
            s_set.remove(s[i])
            s_set.add(s[i+k])
    print(count)

if __name__ == "__main__":
    main()
