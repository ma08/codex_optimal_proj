

def main():
    y, p = input().split()  # y is the word, p is the punctuation
    if y[-1] == 'e':  # if the word ends with e
        print(y + 'x' + p)  # add an x and the punctuation
    elif y[-1] in 'aiou':  # if the word ends with a, i, o, or u
        print(y[:-1] + 'ex' + p)  # remove the last letter and add ex and the punctuation
    else:
        print(y + p)  # otherwise, just add the punctuation

if __name__ == "__main__":
    main()
