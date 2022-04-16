

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
    count = 0
    for i in range(0, n):
        for j in range(i+1, n+1):
            #print(s[i:j])
            if set(s[i:j]).issubset(available_chars):
                count += j-i
            #s_set.remove(s[j])
    print(count)

if __name__ == "__main__":
    main()
