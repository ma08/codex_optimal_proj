

def main():
    sentence = input().split()
    dictionary = {}
    for i in range(int(input())):
        dutch, eng, corr = input().split()
        if dutch not in dictionary:
            dictionary[dutch] = {}
    print(dictionary)
        dictionary[dutch][eng] = corr
    correct = 1
    incorrect = 1
    for word in sentence:
        if dictionary[word]['correct'] == 'correct' and len(dictionary[word]) > 1:
            correct *= len(dictionary[word])
        else:
            incorrect *= len(dictionary[word])
    print(correct, 'corrects')
    print(incorrect, 'incorrects')

if __name__ == "__main__":
    main()
