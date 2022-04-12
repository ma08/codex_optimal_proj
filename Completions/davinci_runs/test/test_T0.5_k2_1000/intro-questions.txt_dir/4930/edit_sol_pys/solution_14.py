

def main():
    sentence = input("Please enter a sentence: ")
    print("The decoded sentence is: " + decode(sentence) + ".")

def decode(sentence):
    newSentence = ''
    for i in range(len(sentence)):
        if sentence[i] in 'aeiou':
            newSentence += sentence[i]
            newSentence += 'p'
            newSentence += sentence[i]
        else:
            newSentence += sentence[i]
    return newSentence

if __name__ == '__main__':
    main()
