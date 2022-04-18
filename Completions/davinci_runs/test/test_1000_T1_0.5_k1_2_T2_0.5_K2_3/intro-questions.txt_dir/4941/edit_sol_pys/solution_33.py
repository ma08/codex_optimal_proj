

def main():
    with open('input.txt', 'r') as file:
        sentence = file.readline()
        sentence = sentence.split()
        dictionary = {}
        for i in range(int(file.readline())):
            dutch, eng, corr = file.readline().split()
            if dutch not in dictionary:
                dictionary[dutch] = {}
            dictionary[dutch][eng] = corr
        correct = 1
        incorrect = 1
        for word in sentence:
            if dictionary[word]['correct'] == 'correct\n':
                correct *= len(dictionary[word])
            else:
                incorrect *= len(dictionary[word])
        with open('output.txt', 'w') as output:
            output.write(str(correct) + ' correct\n' + str(incorrect) + ' incorrect\n')

if __name__ == "__main__":
    main()
