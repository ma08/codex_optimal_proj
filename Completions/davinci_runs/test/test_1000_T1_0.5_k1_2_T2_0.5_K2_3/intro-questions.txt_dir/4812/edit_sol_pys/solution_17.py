

with open('input.txt', 'r') as inp:
    S = inp.readline().strip()
    E = int(inp.readline())
    endings = []
    for i in range(E):
        endings.append(inp.readline().strip().split())
    P = int(inp.readline())
    phrases = []
    for i in range(P):
        phrases.append(inp.readline().strip().split())

    def check(word):
        for i in endings:
            if word in i:
                return i
        return False

    with open('output.txt', 'w') as out:
        for phrase in phrases:
            if len(phrase) == 2: # если предложение содержит два слова
                if check(phrase[1]) and check(S[-len(phrase[1]):]):
                    if check(phrase[1]) == check(S[-len(phrase[1]):]):
                        out.write("YES\n")
                    else:
                        out.write("NO\n")
                else:
                    out.write("NO\n")
            else:
                if check(phrase[1]) and check(phrase[2]) and check(S[-len(phrase[2]):]):
                    if check(phrase[1]) == check(phrase[2]) and check(phrase[2]) == check(S[-len(phrase[2]):]):
                        out.write("YES\n")
                    else:
                        out.write("NO\n")
                else:
                    out.write("NO\n")
