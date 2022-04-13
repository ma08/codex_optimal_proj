

from collections import defaultdict

def main():
    num_patrons = int(input())
    patrons = defaultdict(set)
    for i in range(num_patrons):
        patron, language, *other_languages = input().split()
        patrons[patron].add(language)
        for other_language in other_languages:
            patrons[patron].add(other_language)
    print(solve(patrons))

if __name__ == "__main__":
    main()
