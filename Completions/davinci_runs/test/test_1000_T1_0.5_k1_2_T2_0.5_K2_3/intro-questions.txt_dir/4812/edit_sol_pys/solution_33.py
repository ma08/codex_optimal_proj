

S = "drought"
E = 2
endings = []
endings.append(set("aught ought aut acht".split()))
endings.append(set("ought oubt outte out oute".split()))
P = 5
phrases = []
phrases.append("tasty sprout")
phrases.append("difficult route")
phrases.append("worried and fraught")
phrases.append("forever in doubt")
phrases.append("apples and pears")


S = input()
E = int(input())
endings = []
for _ in range(E):
    endings.append(set(input().split()))
P = int(input())
phrases = []
for _ in range(P):
    phrases.append(input().split())
#S = "hello"
#E = 1
#endings = [set("ello".split())]
#P = 2
#phrases = [["hello"], ["hello", "world"]]

for phrase in phrases:
    words = phrase
    for word in words:
        for ending in endings:
            if word.endswith(tuple(ending)):
                if words[-1] == word:
                    print("YES")
                else:
                    print("NO")
