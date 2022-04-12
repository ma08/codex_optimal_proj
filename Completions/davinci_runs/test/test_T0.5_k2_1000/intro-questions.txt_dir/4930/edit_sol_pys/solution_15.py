

def main():
    sentence = input("Enter a sentence: ")
    print(encode(sentence)) # print the encoded sentence

def encode(sentence):
    newSentence = '' # empty string
    for i in range(len(sentence)):
        if sentence[i] in 'aeiou': # if the letter is a vowel
            newSentence += sentence[i]
            newSentence += 'p' # add a p
            newSentence += sentence[i]
        else: # if the letter is not a vowel
            newSentence += sentence[i]
    return newSentence

if __name__ == '__main__':
    main()
