

from sys import stdin
from collections import defaultdict
from itertools import permutations

def main():
    n = int(stdin.readline())
    sentence = stdin.readline().rstrip().split()
    m = int(stdin.readline())
    dictionary = defaultdict(list)
    for _ in range(m):
        dutch, english, correct = stdin.readline().rstrip().split()
        dictionary[dutch].append((english, correct))
    
    if all(len(dictionary[word]) == 1 for word in sentence) and all(dictionary[word][0][1] == 'correct' for word in sentence):
        print(' '.join(dictionary[word][0][0] for word in sentence))
        print('correct')
    else:
        correct_sentences = 0
        incorrect_sentences = 0
        for permutation in permutations(sentence):
            if all(len(dictionary[word]) == 1 for word in permutation):
                correct_sentences += 1
            else:
                incorrect_sentences += 1
        print(correct_sentences, 'correct', sep=' ')
        print(incorrect_sentences, 'incorrect', sep=' ')

main()
