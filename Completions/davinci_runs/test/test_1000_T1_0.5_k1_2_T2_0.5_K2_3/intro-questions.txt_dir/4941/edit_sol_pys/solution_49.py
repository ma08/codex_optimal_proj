

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
        if dictionary[word]['correct'] == 'correct' or dictionary[word]['correct'] == 'incorrect':
            correct += len(dictionary[word])
        else:
            incorrect += len(dictionary[word])
    print(correct, 'correct', incorrect, 'incorrect')

if __name__ == "__main__":
    main()
