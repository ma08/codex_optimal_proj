

def main():
    """
    Main function
    """
    n = int(input())
    k = int(input())
    s = list(input())
    available_chars = input().split()
    #print(n, k)
    #print(s)
    #print(available_chars)
    # s_set = set(s)
    # print(s_set)
    # print(available_chars)
    # count = 0
    # for i in range(1, n+1):
    #     for j in range(0, n-i+1):
    #         if s_set.issubset(available_chars):
    #             count += 1
    #         s_set.remove(s[j])
    # print(count)

if __name__ == "__main__":
    main()
