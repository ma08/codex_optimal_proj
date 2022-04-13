

def check(word, endings):
    for ending in endings:
        if word in ending:
            return ending
    return False


def check_phrase(phrase, word, endings):
    return check(phrase[1], endings) == check(phrase[2], endings) and check(phrase[2], endings) == check(word[-len(phrase[2]):], endings)



def main():
    with open('file.txt', 'r') as f:
        S = f.readline()
        E = int(f.readline())
        endings = []
        for i in range(E):
            endings.append(f.readline().split())
        P = int(f.readline())
        phrases = []
        for i in range(P):
            phrases.append(f.readline().split())
        for phrase in phrases:
            if check_phrase(phrase, S, endings) is True:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
