

def main():
    sentence = input()
    print(encode(sentence))

def encode(sentence):
    newSentence = ''
    for i in range(len(sentence)):
        if sentence[i] in 'aeiouAEIOU':
            newSentence += sentence[i]
            newSentence += 'p'
            newSentence += sentence[i]
        else:
            newSentence += sentence[i]
    return newSentence

if __name__ == '__main__':
    main()
