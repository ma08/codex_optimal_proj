

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
        if dictionary[word]['correct'] == 'correct' and len(dictionary[word]) > 1:
            correct *= len(dictionary[word])
        elif len(dictionary[word]) > 1:
            incorrect *= len(dictionary[word])
    print(correct, 'correct')
    print(incorrect, 'incorrect')

if __name__ == "__main__":
    main()
