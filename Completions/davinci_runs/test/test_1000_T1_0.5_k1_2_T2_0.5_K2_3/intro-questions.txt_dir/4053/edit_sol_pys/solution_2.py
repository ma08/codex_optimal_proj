

def game(n, words): 
    prefixes = [words[0]] 
    suffixes = [words[1]] 
    for word in words: 
        if word.startswith(prefixes[-1]): 
            prefixes.append(word) 
        else: 
            suffixes.append(word) 
    return ''.join(['P' if word in prefixes else 'S' for word in words]) 


if __name__ == "__main__": 
    n = int(input()) 
    words = [input() for _ in range(2*n-2)] 
    print(game(n, words)) 
