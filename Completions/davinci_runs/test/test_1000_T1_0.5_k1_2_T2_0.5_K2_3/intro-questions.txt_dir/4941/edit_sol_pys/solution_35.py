
from sys import stdin
from collections import defaultdict

def dutch_to_english(dutch_sentence, dutch_to_english, english_to_dutch):
    # dutch_to_english: dict of dutch word to english word
    # english_to_dutch: dict of english word to dutch word
    if len(dutch_sentence) == 0:
        return [""]
    english_words = dutch_to_english[dutch_sentence[0]]
    english_sentences = []
    for english_word in english_words:
        english_sentences += [english_word + " " + sentence for sentence in dutch_to_english(dutch_sentence[1:], dutch_to_english, english_to_dutch)]
    return english_sentences

def english_to_dutch(english_sentence, dutch_to_english, english_to_dutch):
    # dutch_to_english: dict of dutch word to english word
    # english_to_dutch: dict of english word to dutch word
    if len(english_sentence) == 0:
        return [""]
    dutch_words = english_to_dutch[english_sentence[0]]
    dutch_sentences = []
    for dutch_word in dutch_words:
        dutch_sentences += [dutch_word + " " + sentence for sentence in english_to_dutch(english_sentence[1:], dutch_to_english, english_to_dutch)]
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
    english_sentences = dutch_to_english(dutch_sentence, dutch_to_english, english_to_dutch)[1:]
    correct_count = 0
    incorrect_count = 0
    for english_sentence in set(english_sentences):
        if english_sentence in english_to_dutch:
            correct_count += 1
        else:
            incorrect_count += 1
    print(correct_count, "correct")
    print(incorrect_count, "incorrect")

if __name__ == "__main__":
    main()
