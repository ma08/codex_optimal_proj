

def check(word, endings):
    if word == "":
        return False
    for i in endings:
        if word.lower() in i:
            return i
    return False

def check(word, endings):
    for i in endings:
        if word in i:
            return i
    return False

for phrase in phrases:
    if len(phrase) == 2:
        if check(phrase[1], endings) and check(S[-len(phrase[1]):], endings):
            if check(phrase[1], endings) == check(S[-len(phrase[1]):], endings):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if check(phrase[1], endings) and check(phrase[2], endings) and check(S[-len(phrase[2]):], endings):
            if check(phrase[1], endings) == check(phrase[2], endings) and check(phrase[2], endings) == check(S[-len(phrase[2]):], endings):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
