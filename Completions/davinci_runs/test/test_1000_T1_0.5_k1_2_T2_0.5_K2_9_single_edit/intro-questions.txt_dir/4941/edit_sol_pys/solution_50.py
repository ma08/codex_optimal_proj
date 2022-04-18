

def main():
    sentence = input()
    sentence = sentence.split()
    dictionary = {}
    for i in range(int(input())):
        dutch, eng, corr = input().split()
        if dutch not in dictionary:
            dictionary[dutch] = {}
        dictionary[dutch][eng] = corr
    correct = 1
    incorrect = 1
    for word in sentence:
        if dictionary[word]['correct'] == 'correct':
            correct *= len(dictionary[word])
        else:
            incorrect *= len(dictionary[word])
    print(correct, 'correct', end=' ')
    print(incorrect, 'incorrect', end=' ')

if __name__ == "__main__":
    main()
