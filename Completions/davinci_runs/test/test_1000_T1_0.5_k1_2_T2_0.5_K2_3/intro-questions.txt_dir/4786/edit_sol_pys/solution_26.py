

#%%

def main():
    n = int(input())
    keywords = [input() for _ in range(n)]
    keywords = list(set(keywords))
    for i in range(len(keywords)):
        for j in range(i+1, len(keywords)):
            #print(i, j)
            if keywords[i].lower().replace('-', ' ') == keywords[j].lower().replace('-', ' '):
                #print(keywords[i], keywords[j])
                keywords[i] = ''
                keywords[j] = ''
    keywords = list(set(keywords))
    try:
        keywords.remove('')
    except ValueError:
        pass
    print(len(keywords))

main()

#%%

#%%

def main():
    n = int(input())
    keywords = [input() for _ in range(n)]
    keywords = list(set(keywords))
    for i in range(len(keywords)):
        for j in range(i+1, len(keywords)):
            #print(i, j)
            if keywords[i].lower().replace('-', ' ') == keywords[j].lower().replace('-', ' '):
                #print(keywords[i], keywords[j])
                keywords[i] = ''
                keywords[j] = ''
    keywords = list(set(keywords))
    try:
        keywords.remove('')
    except ValueError:
        pass
    print(len(keywords))

main()
