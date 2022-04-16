

def main():
    y, p = input().split() # y is the word, p is the pronoun
    if y[-1] == "e": # if the word ends with e
        print(y + "x" + p) # add x to the end
    elif y[-1] in "aiou": # if the word ends with a vowel
        print(y[:-1] + "ex" + p) # remove the last letter, add ex
    elif y[-2:] == "ex": # if the word ends with ex
        print(y + p) # add the pronoun to the end

if __name__ == "__main__":
    main()
