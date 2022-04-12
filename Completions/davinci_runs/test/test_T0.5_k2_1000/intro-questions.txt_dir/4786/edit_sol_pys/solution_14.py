

#%%

def main():
    n = int(input())
    words = [input() for _ in range(n)]
    words = set(words)
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i].lower().replace('-', ' ') == words[j].lower().replace('-', ' '):
                words[i] = ''
                words[j] = ''
    words = set(words)
    words.remove('')
    print(len(words))

main()

#%%
