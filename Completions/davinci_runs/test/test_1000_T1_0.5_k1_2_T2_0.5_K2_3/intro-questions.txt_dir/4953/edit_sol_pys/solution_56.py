

import sys
import re

def main():
    cantina = {} #cantina[name] = primary_language
    patrons = {} #patrons[language] = [name]

    #read in cantina
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        line = sys.stdin.readline().strip()
        m = re.match(r"(.*)\s(.*)\s(.*)", line)
        name, primary_language, others = m.groups()
        cantina[name] = primary_language
        patrons[primary_language] = [name]
        for other_language in others.split():
            if other_language not in patrons:
                patrons[other_language] = []
            patrons[other_language].append(name)

    print(cantina)
    print(patrons)

    #find minimum number of patrons to remove
    min_patrons = N
    for lang, names in patrons.items():
        if len(names) == 1:
            continue
        else:
            print(names)
            print(patrons)
            print(cantina)
            print(lang)
            print(patrons[lang])
            print(cantina[patrons[lang][0]])
            print(patrons[cantina[patrons[lang][0]]])
            if len(patrons[cantina[patrons[lang][0]]]) == 1:
                continue
            else:
                min_patrons = min(min_patrons, N - len(patrons[cantina[patrons[lang][0]]]))

    print(min_patrons)

if __name__ == "__main__":
    main()
