

import sys, os
import glob
import string
def main():
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".txt"):
            print(os.path.join(cwd, file))
            f = open(file, "r")
            data = f.read()
            f.close()
            print(len(data))
            print(data)
            print(data[0])
            print(data[1])
            print(data[2])
            print(data[-1])
            print(data[-2])
            print(data[-3])
            print(data[0:5])
            print(data[:-5])
            print(data[5:])
            print(data[0:len(data)])
            print(data.replace("\n", " "))
            print(data.replace("\t", " "))
            print(data.replace("\n", " ").replace("\t", " "))
            print(string.punctuation)
            print(data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)))
            print(data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)).split())
            print(len(data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)).split()))
            print(data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)).split()[0])
            print(data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)).split()[-1])
            print(data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)).split()[0:5])
            print(data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)).split()[-5:])
            print(data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)).split()[0:len(data)])
            for word in data.replace("\n", " ").replace("\t", " ").translate(str.maketrans('', '', string.punctuation)).split():
                print(word)
                print(len(word))
                print(word[0])
                print(word[-1])
                print(word[0:5])
                print(word[-5:])
                print(word[0:len(word)])
                print(word.upper())
                print(word.lower())
                print(word.replace("e", "3"))
                print(word.replace("o", "0"))
                print(word.replace("e", "3").replace("o", "0"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1").replace("E", "3"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1").replace("E", "3").replace("O", "0"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1").replace("E", "3").replace("O", "0").replace("A", "4"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1").replace("E", "3").replace("O", "0").replace("A", "4").replace("I", "1"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1").replace("E", "3").replace("O", "0").replace("A", "4").replace("I", "1").replace("T", "7"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1").replace("E", "3").replace("O", "0").replace("A", "4").replace("I", "1").replace("T", "7").replace("S", "5"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1").replace("E", "3").replace("O", "0").replace("A", "4").replace("I", "1").replace("T", "7").replace("S", "5").replace("B", "8"))
                print(word.replace("e", "3").replace("o", "0").replace("a", "4").replace("i", "1").replace("t", "7").replace("s", "5").replace("b", "8").replace("g", "6").replace("l", "1").replace("E", "3").replace("O", "0").replace("A", "4").replace("I", "1").replace("T", "7").replace("S", "5").replace("B", "8").replace("G", "6"))
               

if __name__ == "__main__":


    main()
