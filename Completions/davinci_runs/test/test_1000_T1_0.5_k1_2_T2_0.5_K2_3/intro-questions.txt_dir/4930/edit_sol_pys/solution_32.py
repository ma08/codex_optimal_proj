

def main():
    sentence = input("Enter a sentence: ")
    print(decode(sentence))


def decode(sentence):
    new_sentence = ''
    for i in range(len(sentence)):
        if sentence[i] in 'aeiou':
            new_sentence += sentence[i]
            new_sentence += 'p'
            new_sentence += sentence[i]
        else:
            new_sentence += sentence[i]
    return new_sentence


if __name__ == '__main__':
    main()
