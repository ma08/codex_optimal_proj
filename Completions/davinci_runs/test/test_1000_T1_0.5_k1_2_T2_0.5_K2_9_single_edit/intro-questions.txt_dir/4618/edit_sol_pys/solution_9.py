def main():
    s = input()     # input string
    k = int(input())    # kth smallest substring
    substr = []
    for i in range(len(s)):     # loop through the string
        for j in range(i+1, len(s)+1):    # loop through the string again
            substr.append(s[i:j]) # append the substring
    substr.sort()
    print(substr[k-1])

if __name__ == "__main__":
    main()
