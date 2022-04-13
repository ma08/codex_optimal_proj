

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
# endings.append(set("aught ought aut acht".split()))  # words that end with "aught"
# endings.append(set("ought oubt outte out oute".split()))  # words that end with "ought"
# P = 5
# phrases = []
# phrases.append("tasty sprout")
# phrases.append("difficult route")
# phrases.append("worried and fraught")
# phrases.append("forever in doubt")
# phrases.append("apples and pears")

for phrase in phrases:
    words = phrase.split()
    for ending in endings:
        for word in words:
            if word.endswith(tuple(ending)):
                print("YES")  # print YES if any word in the phrase ends with any of the endings
                break  # if any word in the phrase ends with any of the endings, no need to check the rest of the words
    else:  # if no word in the phrase ends with any of the endings
        print("NO")  # print NO
