

def main():
    # Read input
    n = int(input())
    keywords = set()
    for i in range(n):
        keyword = input()
        keywords.add(keyword.lower().replace('-', ' '))
    # Find similar keywords.
    # Print result
    print(len(keywords))

if __name__ == '__main__':
    main()
