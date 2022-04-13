

from collections import defaultdict, Counter

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(Counter)
    for i in range(m):
        dutch, english, correct = input().split() # dutch word, english word, whether the translation is correct or not
        d[dutch].update({english: correct}) # dutch word, (english word, whether the translation is correct or not)
    correct = 1
    incorrect = 0
    for word in s:
        correct *= len([c for e, c in d[word].items() if c == 'correct'])
        incorrect += len([c for e, c in d[word].items() if c == 'incorrect'])
    print(correct)
    print(incorrect)

main()
