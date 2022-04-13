
import sys

def main():
    word = sys.stdin.readline().strip()  # read a line
    new_word = "" # initialize string
    for i in range(0, len(word)):
        if word[i] in "aeiou":  # if character is vowel
            new_word += word[i] + "p" + word[i]  # add p before and after it
        else:
            new_word += word[i]  # if not, add the character as is
    print(new_word)  # print the new string

if __name__ == "__main__":
    main()
