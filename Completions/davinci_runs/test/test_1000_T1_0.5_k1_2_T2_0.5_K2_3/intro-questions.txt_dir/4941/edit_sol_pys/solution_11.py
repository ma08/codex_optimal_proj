
# Gets input
n = int(input())
s = input().split()
m = int(input())
translations = []
for i in range(m):
    translations.append(input().split())

# Builds a dictionary of the translations and marks whether they are correct or not
translations_dictionary = {}
for i in range(m):
    if translations[i][0] not in translations_dictionary:
        translations_dictionary[translations[i][0]] = [[translations[i][1], translations[i][2] == "correct"]]
    else:
        translations_dictionary[translations[i][0]].append([translations[i][1], translations[i][2] == "correct"])

# Finds all the possible translations of the sentence
possible_translations = []
def find_translations(i, translation):
    if i == n:
        possible_translations.append(translation)
    else:
        for j in range(len(translations_dictionary[s[i]])):
            find_translations(i+1, translation + " " + translations_dictionary[s[i]][j][0])

# Finds the number of correct and incorrect translations and prints the result
find_translations(0, "")
correct_translations = 0
incorrect_translations = 0
for i in range(len(possible_translations)):
    correct = True
    for j in range(m):
        if possible_translations[i].find(translations[j][1]) != -1:
            if translations[j][2] == "incorrect":
                correct = False
    if correct:
        correct_translations += 1
    else:
        incorrect_translations += 1
if correct_translations == 0 and incorrect_translations == 0:
    print("impossible")
elif correct_translations == 1 and incorrect_translations == 0:
    print(possible_translations[0][1:])
    print("correct")
elif correct_translations == 0 and incorrect_translations == 1:
    print(possible_translations[0][1:])
    print("incorrect")
else:
    print(correct_translations, "correct")
    print(incorrect_translations, "incorrect")
