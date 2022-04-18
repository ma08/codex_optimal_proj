

from collections import defaultdict

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(list)
    for i in range(m):
        dutch, english, correct = input().split() # dutch word, english word, whether the translation is correct or not
        d[dutch].append((english, correct)) # dutch word, (english word, whether the translation is correct or not)
    correct = 0
    incorrect = 1
    for word in s:
        correct *= len([c for e, c in d[word] if c == 'correct'])
        incorrect += len([c for e, c in d[word] if c == 'incorrect'])
    print(correct)
    print(incorrect)

main()
