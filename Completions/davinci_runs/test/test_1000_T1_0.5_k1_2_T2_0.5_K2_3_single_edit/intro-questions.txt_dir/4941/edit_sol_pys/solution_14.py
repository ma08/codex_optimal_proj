

# Gets the input
n = int(input())
s = input().split()
m = int(input())
translations = []
for i in range(m):
    translations.append(input().split())

# Builds a dictionary of the translations
translations_dictionary = {}
for i in range(m):
    if translations[i][0] not in translations_dictionary:
        translations_dictionary[translations[i][0]] = [translations[i][1]]
    else:
        translations_dictionary[translations[i][0]].append(translations[i][1])

# Finds all the possible translations of the sentence and the number of correct and incorrect translations
possible_translations = []
correct_translations = 0
incorrect_translations = 0
def find_translations(i, translation, correct):
    if i == n:
        if correct:
            correct_translations += 1
        else:
            incorrect_translations += 1
        possible_translations.append([translation, correct])
    else:
        for j in range(len(translations_dictionary[s[i]])):
            find_translations(i+1, translation + " " + translations_dictionary[s[i]][j], correct)
        for j in range(m):
            if s[i] == translations[j][0]:
                find_translations(i+1, translation + " " + translations[j][1], correct and translations[j][2] == "correct")
find_translations(0, "", True)

# Prints the result
if correct_translations == 0 and incorrect_translations == 0:
    print("impossible")
elif correct_translations == 1 and incorrect_translations == 0:
    print(possible_translations[0][0][1:])
    print("correct")
elif correct_translations == 0 and incorrect_translations == 1:
    print(possible_translations[0][0][1:])
    print("incorrect")
else:
    print(correct_translations, "correct")
    print(incorrect_translations, "incorrect")
