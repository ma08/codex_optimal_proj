

def main():
    s = input()  # input string
    k = int(input())
    substr = []  # list of all substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr.append(s[i:j])
    substr.sort()
    print(substr[k-1])


if __name__ == '__main__':
    main()
