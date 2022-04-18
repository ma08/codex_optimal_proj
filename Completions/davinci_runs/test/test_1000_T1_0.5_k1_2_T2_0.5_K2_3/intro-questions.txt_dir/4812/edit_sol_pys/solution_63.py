

S = input()
E = int(input())
endings = {}
for i in range(E):
    endings[input()] = input()
P = int(input())
phrases = []
for i in range(P):
    phrases.append(input().split())

def check(word):
    return endings.get(word)

for phrase in phrases:
    if len(phrase) == 2:
        if check(phrase[1]) and check(S[-len(phrase[1]):]):
            if check(phrase[1]) == check(S[-len(phrase[1]):]):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if check(phrase[1]) and check(phrase[3]) and check(S[-len(phrase[3]):]):
            if check(phrase[1]) == check(phrase[3]) and check(phrase[3]) == check(S[-len(phrase[3]):]):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
