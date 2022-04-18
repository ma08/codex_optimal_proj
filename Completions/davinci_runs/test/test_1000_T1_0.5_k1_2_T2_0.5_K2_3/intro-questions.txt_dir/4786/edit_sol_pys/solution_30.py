
def main():
    n = int(input())
    keywords = [input() for _ in range(n)]
    keywords = list(set(keywords))
    for i in range(len(keywords)):
        for j in range(i+1, len(keywords)):
            #print(i, j)
            if keywords[i].lower().replace('-', ' ') == keywords[j].lower().replace('-', ' ') and keywords[i] != '':
                #print(keywords[i], keywords[j])
                keywords[i] = ''
                keywords[j] = ''
    print(len(keywords))

main()
