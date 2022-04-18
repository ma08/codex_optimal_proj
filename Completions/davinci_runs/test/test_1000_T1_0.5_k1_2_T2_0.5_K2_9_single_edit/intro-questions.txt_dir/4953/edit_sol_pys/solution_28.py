
import sys

def main():
    n = int(sys.stdin.readline()) # read the first line
    languages = []
    for i in range(n):
        line = sys.stdin.readline().rstrip().split() # read the next line
        for lang in line[2:]: # if the language is in the list, add it
            if lang not in languages:
                languages.append(lang)
    print(len(languages)) # print the number of languages

main()
