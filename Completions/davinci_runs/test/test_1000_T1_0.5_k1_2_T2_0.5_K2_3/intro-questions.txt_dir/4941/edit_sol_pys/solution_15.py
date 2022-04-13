
from sys import stdin
from collections import defaultdict

def dutch_to_english(dutch_sentence, dutch_to_english, english_to_dutch, english_sentence=""):
    # dutch_to_english: dict of dutch word to english word
    # english_to_dutch: dict of english word to dutch word
    if len(dutch_sentence) == 0 and len(english_sentence) > 0:
        return [english_sentence]
    english_words = dutch_to_english[dutch_sentence[0]]
    english_sentences = []
    for english_word in english_words:
        english_sentences += dutch_to_english(dutch_sentence[1:], dutch_to_english, english_to_dutch, english_sentence + english_word + " ") # fix here
    return english_sentences

def english_to_dutch(english_sentence, dutch_to_english, english_to_dutch, dutch_sentence=""):
    # dutch_to_english: dict of dutch word to english word
    # english_to_dutch: dict of english word to dutch word
    if len(english_sentence) == 0 and len(dutch_sentence) > 0:
        return [dutch_sentence]
    dutch_words = english_to_dutch[english_sentence[0]]
    dutch_sentences = []
    for dutch_word in dutch_words:
        dutch_sentences += dutch_to_english(english_sentence[1:], dutch_to_english, english_to_dutch, dutch_sentence + dutch_word + " ") # fix here
    return dutch_sentences

def main():
    n = int(stdin.readline())
    dutch_sentence = stdin.readline().split()
    m = int(stdin.readline())
    dutch_to_english = defaultdict(set)
    english_to_dutch = defaultdict(set)
    for _ in range(m):
        dutch, english, correct = stdin.readline().split()
        dutch_to_english[dutch].add(english)
        english_to_dutch[english].add(dutch)
    english_sentences = dutch_to_english(dutch_sentence, dutch_to_english, english_to_dutch, "")
    correct_count = 0
    incorrect_count = 0
    for english_sentence in english_sentences:
        if english_sentence.strip() in english_to_dutch:
            correct_count += 1
        else:
            incorrect_count += 1
    print(correct_count, "correct")
    print(incorrect_count, "incorrect")

if __name__ == "__main__":
    main()
