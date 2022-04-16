

def main():
    n = int(input())
    keywords = []
    for i in range(n):
        keyword = input()
        keywords.append(keyword.lower().replace('-', ' '))
    similar = []
    for i in range(n):
        for j in range(n):
            if i != j and keywords[i] == keywords[j]:
                similar.append(i)
                similar.append(j)
    print(n - len(set(similar)))

if __name__ == '__main__':
    main()
