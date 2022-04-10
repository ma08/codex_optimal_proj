

n = int(input())
words = input().split()

#print(n, words)

def get_abbreviations(words):
    abbreviations = ""
    for word in words:
        abbreviations += word[0]
    return abbreviations.upper()

def get_abbreviations_length(words):
    return len(get_abbreviations(words))

def get_length_after_abbreviation(words):
    length = 0
    for word in words:
        length += len(word)
    return length - get_abbreviations_length(words)

def get_length_after_abbreviation_with_space(words):
    return len(words) - 1 + get_length_after_abbreviation(words)

def get_max_possible_abbreviation_length(words):
    abbreviation = ""
    for word in words:
        if word[0].isupper():
            abbreviation += word[0]
        else:
            break
    return len(abbreviation)

def get_max_possible_abbreviation_length_with_space(words):
    return len(words) - 1 + get_max_possible_abbreviation_length(words)

def get_min_length_after_one_abbreviation(n, words):
    if n <= 1:
        return n
    else:
        if get_max_possible_abbreviation_length_with_space(words) < get_length_after_abbreviation_with_space(words):
            return get_max_possible_abbreviation_length_with_space(words)
        else:
            return get_length_after_abbreviation_with_space(words)

print(get_min_length_after_one_abbreviation(n, words))
