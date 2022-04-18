

peter_pan_frames = [
    "..#..\n",
    ".#.#.\n",
    "#.X.#\n",
    ".#.#.\n",
    "..#..\n"
    ]

wendy_frames = [
    "..*..\n",
    ".*.*.\n",
    "*.X.*\n",
    ".*.*.\n",
    "..*..\n"
    ]

def create_frames(word, frame):
    frame_word = wendy_frames[0]
    for i in range(1, len(word)):
        frame_word += peter_pan_frames[0]
    frame_word += wendy_frames[1]
    for i in range(1, len(word)):
        frame_word += peter_pan_frames[1]
    frame_word += wendy_frames[2].replace("X", word[0])
    for i in range(1, len(word)):
        frame_word += peter_pan_frames[2].replace("X", word[i])
    frame_word += wendy_frames[3]
    for i in range(1, len(word)):
        frame_word += peter_pan_frames[3]
    frame_word += wendy_frames[4]
    for i in range(1, len(word)):
        frame_word += peter_pan_frames[4]
    return frame_word

word = input()
print(create_frames(word, peter_pan_frames))
