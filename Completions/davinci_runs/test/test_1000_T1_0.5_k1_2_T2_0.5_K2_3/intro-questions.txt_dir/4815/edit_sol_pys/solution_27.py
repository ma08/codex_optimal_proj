

# def main():
#     n, p, m = [int(x) for x in input().split()]
#     names = [input() for _ in range(n)]
#     scores = {name:0 for name in names}
#     for _ in range(m):
#         name, score = input().split()
#         scores[name] += int(score)
#         if scores[name] >= p:
#             print(name, "wins!")
#             return
#     print("No winner!")
#
# if __name__ == '__main__':
#     main()

import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    return [word for word in words if re.search(regex, word)]

print(get_matching_words(r"v"))
print(get_matching_words(r"ss"))
print(get_matching_words(r"e$"))
print(get_matching_words(r"b.b"))
print(get_matching_words(r"b.+b"))
print(get_matching_words(r"b.*b"))
print(get_matching_words(r"(b.b)+"))
print(get_matching_words(r"a.e.i.o.u"))
print(get_matching_words(r"^[a-z]+$"))
print(get_matching_words(r"^[regular expression]+$"))
print(get_matching_words(r"([a-z].)+[a-z]$"))
print(get_matching_words(r"([a-z]).+[a-z]$"))
print(get_matching_words(r"[a-z]+$"))
