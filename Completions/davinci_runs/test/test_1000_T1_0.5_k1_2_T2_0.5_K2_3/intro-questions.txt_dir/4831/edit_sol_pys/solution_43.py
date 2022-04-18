

peterpan_frame = [
    "..#..", ".#.#.", "#.X.#", ".#.#.", "..#.."
]

wendy_frame = [
    "..*..", ".*.*.", "*.X.*", ".*.*.", "..*.."
]

    def create_frame(word, frame):
    frame_word = ""
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frame[0]
        else:
            frame_word += peterpan_frame[0]
    frame_word += "\n"
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frame[1]
        else:
            frame_word += peterpan_frame[1]
    frame_word += "\n"
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frame[2].replace("X", word[i])
        else:
            frame_word += peterpan_frame[2].replace("X", word[i])
    frame_word += "\n"
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frame[3]
        else:
            frame_word += peterpan_frame[3]
    frame_word += "\n"
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frame[4]
        else:
            frame_word += peterpan_frame[4]
    frame_word += "\n"
    return frame_word


def main():
    word = input()
    print(create_frame(word, peterpan_frame))


if __name__ == "__main__":
    main()
