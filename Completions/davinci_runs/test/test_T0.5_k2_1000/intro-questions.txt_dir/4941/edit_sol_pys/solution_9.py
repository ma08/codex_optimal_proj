

from collections import defaultdict

def main():
    n = int(input())
    s = input().split() #s is the list of words
    m = int(input())
    d = defaultdict(list) #d is the dictionary
    for i in range(m):
        dutch, english, correct = input().split() #dutch is the word, english is the translation, correct is whether it is correct or not, all separated by spaces
        d[dutch].append((english, correct)) #d is a dictionary with the dutch word as key, and a list of tuples of english words and whether they are correct or not, separated by commas
    correct = 1 #correct is the number of correct translations
    incorrect = 0 #incorrect is the number of incorrect translations
    for word in s:
        correct *= len([c for e, c in d[word] if c == 'correct']) #correct is the number of correct translations for each word in s
        incorrect += len([c for e, c in d[word] if c == 'incorrect']) #incorrect is the number of incorrect translations for each word in s
    print(correct)
    print(incorrect)

main()
