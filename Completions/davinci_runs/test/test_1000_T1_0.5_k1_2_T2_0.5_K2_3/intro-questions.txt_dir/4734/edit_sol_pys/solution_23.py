

def main():
    y, p = input().split() #y is the verb, p is the pronoun
    if y[-1] == 'e': #if verb ends in e
        print(y + 'x' + p) #add x to verb
    elif y[-1] in 'aiou': #if verb ends in a vowel
        print(y[:-1] + 'x' + p) #remove last letter of verb and add x
    else:
        print(y + p) #if verb ends in consonant just add pronoun

if __name__ == "__main__":
    main()
