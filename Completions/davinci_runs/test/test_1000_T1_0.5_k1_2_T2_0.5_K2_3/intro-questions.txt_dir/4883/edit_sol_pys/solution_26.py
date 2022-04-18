

import sys

def main():
    lines = sys.stdin.readlines()
    m = int(lines[0].split()[0])
    n = int(lines[0].split()[1])
    translations = {}
    for i in range(1, m + 1):
        translations[lines[i][0]] = lines[i][2].strip()
        translations[lines[i][2].strip()] = lines[i][0]
    for i in range(m + 1, m + 1 + n):
        word1 = lines[i].split()[0].strip()
        word2 = lines[i].split()[1].strip()
        if len(word1) != len(word2):
            print("no")
            continue
        else:
            for j in range(len(word1)):
                if word1[j] != word2[j]:
                    # Try to translate
                    if word1[j] in translations:
                        if translations[word1[j]] == word2[j]:
                            continue
                        else:
                            print("no")
                            break
                    else:
                        print("no")
                        break
                else:
                    continue
            else:
                print("yes")

main()
