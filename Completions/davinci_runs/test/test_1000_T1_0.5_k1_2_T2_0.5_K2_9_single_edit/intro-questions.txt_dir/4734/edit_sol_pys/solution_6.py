

def main():
    y, p = input().split() #input
    if y[-1] == "e": #check if last letter of y is e
        print(y + "x" + p) #add x after the word
    elif y[-1] in "aiou": #check if last letter of y is a vowel
        print(y[:-1] + "ex" + p) #add ex after the word
    elif y[-2:] == "ex": #check if last 2 letters of y are ex
        print(y + p) #add p after the word

if __name__ == "__main__":
    main()
