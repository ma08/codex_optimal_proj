

def main():
    n, k = list(map(int, input().split()))
    s = list(input())
    available_chars = set(input().split())  # set of available characters
    s_set = set(s)
    count = 0
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            if s_set.issubset(available_chars):  # check if available chars has all the characters of s_set
                count += 1
            s_set.remove(s[j])  # remove the first element
    print(count)


if __name__ == "__main__":
    main()
