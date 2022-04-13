

S = input()
E = int(input())
endings = []
for i in range(E):
    endings.append(input().strip())
P = int(input())
phrases = []
for i in range(P):
    phrases.append(input().strip())

def check(word):
    for i in endings:
        if word in i:
            return i
    return False

for phrase in phrases:
    if len(phrase) == 2:
        if check(phrase[1]) and check(S[-len(phrase[1]):]) and phrase[1] == S[-len(phrase[1]):]:
                print("YES")
        else:
            print("NO")
    else:
        if check(phrase[1]) and check(phrase[3]) and check(S[-len(phrase[3]):]) and phrase[1] == phrase[3] and phrase[3] == S[-len(phrase[3]):]:
                print("YES")
        else:
            print("NO")
