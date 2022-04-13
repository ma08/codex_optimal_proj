

def check(word, endings):
    for ending in endings:
        if word in ending:
            return ending
    return False


def check_phrase(phrase, S, endings, phrase_length):
    if phrase_length == 2:
        if check(phrase[1], endings) and check(S[-len(phrase[1]):], endings) and check(phrase[1], endings) == check(S[-len(phrase[1]):], endings):
            return True
        return False
    if phrase_length == 3:
        if check(phrase[1], endings) and check(phrase[2], endings) and check(S[-len(phrase[2]):], endings) and check(phrase[1], endings) == check(phrase[2], endings) and check(phrase[2], endings) == check(S[-len(phrase[2]):], endings):
            return True
        return False


def main():
    S = input()
    E = int(input())
    endings = []
    for i in range(E):
        endings.append(input().split())
    P = int(input())
    phrases = []
    for i in range(P):
        phrases.append(input().split() + [len(input().split())])
    for phrase in phrases:
        if check_phrase(phrase, S, endings, phrase[3]) is True:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
