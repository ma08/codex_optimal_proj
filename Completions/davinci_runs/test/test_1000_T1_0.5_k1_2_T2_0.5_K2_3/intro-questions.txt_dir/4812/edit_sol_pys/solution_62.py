
def check(word, endings):
    for ending in endings:
        if word in ending:
            return ending
    return False

def check_phrase(phrase, S, endings):
    if check(phrase[1], endings) and check(S[-len(phrase[1]):], endings):
        if check(phrase[1], endings) == check(S[-len(phrase[1]):], endings):
            return True
        return False
    else:
        if check(phrase[1], endings) == check(phrase[2], endings) and check(phrase[2], endings) == check(S[-len(phrase[2]):], endings):
            return True
        return False


def main():
    S = input()
    E = int(input())
    endings = []
    for _ in range(E):
        endings.append(input().split())
    P = int(input())
    phrases = []
    for _ in range(P):
        phrases.append(input().split())
    for phrase in phrases:
        if check_phrase(phrase, S, endings):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
