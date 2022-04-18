

def main():
    n = int(input())
    sentence = []
    for i in range(n):
        word = input()
        if word != "$":
            sentence.append(word)
        else:
            sentence.append("$")
    number = len(sentence)
    number_string = str(number)
    for i in range(len(sentence)):
        if sentence[i] == "$":
            sentence[i] = number_string
    print(" ".join(sentence))

main()
