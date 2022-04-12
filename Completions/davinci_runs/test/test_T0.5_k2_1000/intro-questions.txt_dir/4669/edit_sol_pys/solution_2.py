

def is_vowel(l): 
    return l in ['a', 'e', 'i', 'o', 'u', 'y'] 

def score_words(w): 
    score = 0 
    for word in w: 
        num_vowels = 0 
        for l in word: 
            if is_vowel(l): 
                num_vowels += 1 
        if num_vowels % 2 == 0: 
            score += 2 
        else: 
            score += 1 
    return score 


n = int(input()) 
words = input().split() 
print(score_words(words)) 
