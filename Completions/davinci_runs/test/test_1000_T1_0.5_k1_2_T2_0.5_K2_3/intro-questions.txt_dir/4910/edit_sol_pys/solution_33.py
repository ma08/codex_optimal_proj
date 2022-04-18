import sys

def main():
    n = int(input())
    costumes = {}
    for i in range(n):
        costume = sys.stdin.readline().strip()
        if costume not in costumes:
            costumes[costume] = 1
        else:
            costumes[costume] += 1
    max_num = max(costumes.values()) # max number of people wearing a costume
    for costume in sorted(costumes):
        if costumes[costume] == max_num:
            print(costume)

if __name__ == "__main__":
    main()
