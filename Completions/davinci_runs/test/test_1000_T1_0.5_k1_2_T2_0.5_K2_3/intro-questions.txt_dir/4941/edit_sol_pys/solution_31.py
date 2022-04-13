

def main():
    sentence = input()
    sentence = sentence.split()
    dictionary = {}
    for i in range(int(input())):
        dutch, eng, corr = input().split()
        if dutch not in dictionary:
            dictionary[dutch] = {}
        dictionary[dutch][eng] = corr
    correct = 0
    incorrect = 0
    for word in sentence:
        if dictionary[word]['correct'] == 'correct' and len(dictionary[word]) > 0:
            correct += len(dictionary[word])
        elif len(dictionary[word]) > 0:
            incorrect += len(dictionary[word])
    print(correct, 'correct')
    print(incorrect, 'incorrect')

if __name__ == "__main__":
    main()
