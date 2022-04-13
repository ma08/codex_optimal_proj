def remove_hyphens(keywords):
    for i in range(len(keywords)):
        keywords[i] = keywords[i].lower().replace('-', ' ')
    return keywords

def main():
    # Read input
    n = int(input())
    keywords = []
    for i in range(n):
        keyword = input()
        keywords.append(keyword)
    keywords = remove_hyphens(keywords)
    # Find similar keywords
    similar = set()
    for i in range(n):
        for j in range(n):
            if i != j and keywords[i] == keywords[j]:
                similar.add(i)
                similar.add(j)
    # Print results
    print(n - len(similar))

if __name__ == '__main__':
    main()
