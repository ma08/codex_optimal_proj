

def is_vowel(character):
    return character in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for character in word:
            if is_vowel(character):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

n = int(input())
words = input().split()
print(score_words(words))
