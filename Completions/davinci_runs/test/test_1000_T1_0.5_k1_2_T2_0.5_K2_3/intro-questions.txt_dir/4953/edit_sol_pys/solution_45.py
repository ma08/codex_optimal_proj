

import sys
import re

def main():
    cantina = {} #cantina[name] = [language]
    patrons = {} #patrons[language] = language

    #read in cantina
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        line = sys.stdin.readline().strip()
        m = re.match(r"(.*)\s(.*)\s(.*)", line)
        name, language, others = m.groups()
        cantina[name] = [language]
        patrons[language] = language
        for lang in others.split():
            if lang not in patrons:
                patrons[lang] = lang
            cantina[name].append(lang)

    #print(cantina)
    #print(patrons)

    #find minimum size set of patrons to remove
    min_patrons = N
    for lang, names in patrons.items():
        if lang == cantina[names[0]][0]:
            continue
        else:
            if len(names) == 1:
                continue
            else:
                min_patrons = min(min_patrons, N - len(names))

    print(min_patrons)

if __name__ == "__main__":
    main()
