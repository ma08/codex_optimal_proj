

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
        if dictionary[word]['correct'] == 'incorrect' and 'correct' in dictionary[word]:
            incorrect *= len(dictionary[word])
        else:
            correct *= len(dictionary[word])
    print(correct, 'correct')
    print(incorrect, 'incorrect')

if __name__ == "__main__":
    main()
