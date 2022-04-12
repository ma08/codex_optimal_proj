

def main():
    sentence = input().split()
    dictionary = {}
    for i in range(int(input())):
        dutch, eng, correct = input().split()
        if dutch not in dictionary:
            dictionary[dutch] = {}
        dictionary[dutch][eng] = correct
    correct = 1
    incorrect = 1
    for word in sentence:
        if dictionary[word]['correct'] == 'correct' or dictionary[word]['correct'] == 'correct.':
            correct *= len(dictionary[word])
        else:
            incorrect *= len(dictionary[word])
    print(correct, 'correct.')
    print(incorrect, 'incorrect.')

if __name__ == "__main__":
    main()
