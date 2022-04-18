

def main():
    # Read input
    n = int(input())
    keywords = set()
    for i in range(n):
        keyword = input()
        keywords.add(keyword.lower().replace('-', ' '))
    # Find similar keywords
    similar = {}
    for i in range(n):
        for j in range(n):
            if i != j and keywords[i] == keywords[j] and (i not in similar or j not in similar):
                similar.add(i)
                similar.add(j)
    # Print result
    print(n - len(similar))

if __name__ == '__main__':
    main()
