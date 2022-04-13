

peter_pan_frames = [
    "..#..", ".#.#.", "#.X.#", ".#.#.", "..#.."
]

wendy_frames = [
    "..*..", ".*.*.", "*.X.*", ".*.*.", "..*.."
]


def create_frames(word, frame):
    frame_word = ""
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frames[0]
        else:
            frame_word += peter_pan_frames[0]
        frame_word += "\n"
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frames[1]
        else:
            frame_word += peter_pan_frames[1]
        frame_word += "\n"
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frames[2].replace("X", word[i])
        else:
            frame_word += peter_pan_frames[2].replace("X", word[i])
        frame_word += "\n"
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frames[3]
        else:
            frame_word += peter_pan_frames[3]
        frame_word += "\n"
    for i in range(len(word)):
        if i % 3 == 0:
            frame_word += wendy_frames[4]
        else:
            frame_word += peter_pan_frames[4]
        frame_word += "\n"
    return frame_word


word = input()
print(create_frames(word, peter_pan_frames))
