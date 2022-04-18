

peterpan_frame = [
    "..#..",
    ".#.#.",
    "#.X.#",
    ".#.#.",
    "..#.."
    ]

wendy_frame = [
    "..*..",
    ".*.*.",
    "*.X.*",
    ".*.*.",
    "..*.."
    ]

def create_frame(word, frame):
    word_frame = "." * len(frame[0]) * len(word) + "\n"
    for i in range(len(frame)):
        for j in range(len(word)):
            if j % 3 == 0:
                word_frame += frame[i].replace("X", word[j])
            else:
                word_frame += frame[i].replace("X", word[j])
        word_frame += "\n"
    word_frame += "." * len(frame[0]) * len(word) + "\n"
    return word_frame

word = input()
print(create_frame(word, wendy_frame))
