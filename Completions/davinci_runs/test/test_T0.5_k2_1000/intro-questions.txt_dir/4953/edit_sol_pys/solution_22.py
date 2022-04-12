

import sys
import re

def main():
    cantina = {} #cantina[name] = language spoken
    patrons = {} #patrons[language] = [name]

    #read in cantina patrons
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        line = sys.stdin.readline().strip()
        m = re.match(r"(.*)\s(.*)\s(.*)", line)
        name, language, others = m.groups()
        cantina[name] = language
        patrons[language] = [name]
        for lang in others.split():
            if lang not in patrons:
                patrons[lang] = []
            patrons[lang].append(name)

    #find minimum size set of patrons to remove from cantina
    min_patrons = N
    for lang, names in patrons.items():
        if len(names) == 1:
            continue
        else:
            if len(patrons[cantina[patrons[lang][0]]]) == 1:
                continue
            else:
                min_patrons = min(min_patrons, N - len(patrons[cantina[patrons[lang][0]]]))

    print(min_patrons)

if __name__ == "__main__":
    main()
