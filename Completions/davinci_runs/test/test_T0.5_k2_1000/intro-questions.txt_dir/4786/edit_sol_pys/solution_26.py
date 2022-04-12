

def main():
    # Read input
    n = int(input())
    keywords = []
    for i in range(n):
        keyword = input()
        keywords.append(keyword.lower().replace('-', ' '))
    # Find duplicate keywords
    duplicate = set()  # use set to avoid duplicates
    for i in range(n):
        for j in range(n):
            if i != j and keywords[i] == keywords[j]:
                duplicate.add(i)
                duplicate.add(j)
    # Print result
    print(n - len(duplicate))

if __name__ == '__main__':
    main()
