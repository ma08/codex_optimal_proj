

from collections import defaultdict

def main():
    n = int(input())
    s = input().split()
    m = int(input())
    d = defaultdict(list)
    for i in range(m):
        dutch, english, correct = input().split() #dutch is the word, english is the translation, correct is whether it is correct or not
        d[dutch].append((english, correct)) #d is a dictionary with the dutch word as key, and a list of tuples of english words and whether they are correct or not
    correct = 0
    incorrect = 1
    for word in s:
        correct += len([c for e, c in d[word] if c == 'correct'])
        incorrect *= len([c for e, c in d[word] if c == 'incorrect'])
    print(correct)
    print(incorrect)

main()
