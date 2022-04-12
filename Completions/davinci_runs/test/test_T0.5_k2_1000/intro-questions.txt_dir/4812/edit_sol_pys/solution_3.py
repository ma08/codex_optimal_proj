

endings = [["a", "e"], ["i", "y"], ["o", "u"]]
phrases = [["a", "e"], ["a", "i", "y"], ["a", "o", "u"], ["e", "i", "y"], ["e", "o", "u"], ["i", "y", "e"], ["i", "y", "o", "u"], ["o", "u", "e"], ["o", "u", "i", "y"]]
S = "a"

def check(word):
    for i in endings:
        if word.lower() in i:
            return i
    return False

for phrase in phrases:
    if len(phrase) == 2:
        if check(phrase[0]) and check(S[-len(phrase[0]):]):
            if check(phrase[0]) == check(S[-len(phrase[0]):]):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if check(phrase[0]) and check(phrase[1]) and check(S[-len(phrase[1]):]):
            if check(phrase[0]) == check(phrase[1]) and check(phrase[1]) == check(S[-len(phrase[1]):]):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
