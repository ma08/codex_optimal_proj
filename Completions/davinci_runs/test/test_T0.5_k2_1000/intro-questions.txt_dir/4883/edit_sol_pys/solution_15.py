

def main():
    m, n = [int(x) for x in input().split()]  # m is number of translations, n is number of words to check.
    translations = {}
    for i in range(m):
        a, b = input().split()
        translations[a] = b  # a is the original word, b is the translated word.
    for i in range(n):
        a, b = input().split()
        match = True  # match is true if the two words are the same.
        if len(a) != len(b):
            match = False  # if the two words aren't the same length, they can't be the same.
        else:
            for j in range(len(a)):
                if a[j] not in translations and a[j] != b[j]:  # if the letter is not in the translation dictionary and is not the same as the other word, then they are not the same.
                    match = False
                    break
                elif a[j] in translations and translations[a[j]] != b[j]:  # if the letter is in the translation dictionary and is not the same as the other word, then they are not the same.
                    match = False
                    break
        if match:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    main()
