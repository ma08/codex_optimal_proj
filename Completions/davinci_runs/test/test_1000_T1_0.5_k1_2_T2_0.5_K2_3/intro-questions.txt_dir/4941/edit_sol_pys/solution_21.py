

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
        for key in dictionary[word]:
            if dictionary[word][key] == 'correct':
                correct += 1
            else:
                incorrect += 1
    print(correct, 'correct')
    print(incorrect, 'incorrect')

if __name__ == "__main__":
    main()
