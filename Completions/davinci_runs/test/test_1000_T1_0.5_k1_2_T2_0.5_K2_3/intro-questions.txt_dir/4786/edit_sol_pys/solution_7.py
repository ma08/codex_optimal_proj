

def main():
    # read input
    n = int(input())
    keywords = []
    for i in range(n):
        keyword = input()
        keywords.append(keyword.lower().replace('-', ' '))
    # find similar keywords.
    similar = set()
    for i in range(n):
        for j in range(n):
            if i != j and keywords[i] == keywords[j]:
                similar.add(i)
                similar.add(j)
    # print result
    print(n - len(similar))

if __name__ == '__main__':
    main()
