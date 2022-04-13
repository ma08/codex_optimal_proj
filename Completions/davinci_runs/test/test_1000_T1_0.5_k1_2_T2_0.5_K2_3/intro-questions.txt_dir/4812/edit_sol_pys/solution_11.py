

S = input()
E = int(input())
endings = []
for _ in range(E):
    endings.append(set(input().split()))
P = int(input())
phrases = []
for _ in range(P):
    phrases.append(input())

# S = "drought"
# E = 2
# endings = []
# endings.append(set("aught ought aut acht outte out oute".split()))
# endings.append(set("ought oubt".split()))
# P = 5
# phrases = []
# phrases.append("tasty sprout")
# phrases.append("difficult route")
# phrases.append("worried and fraught")
# phrases.append("forever in doubt")
# phrases.append("apples and pears")

for phrase in phrases:
    words = phrase.split()
    for word in words:
        for ending in endings:
            if word.endswith(tuple(ending)):
                if words[-1] == word:
                    print("YES")
                else:
                    print("NO")
