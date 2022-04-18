#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function

peterpan_frame = [  # noqa
    "..#..",
    ".#.#.",
    "#.X.#",
    ".#.#.",
    "..#.."
    ]

wendy_frame = [  # noqa
    "..*..",
    ".*.*.",
    "*.X.*",
    ".*.*.",
    "..*.."
    ]

def create_frame(word, frame):
    frame_word = ""
    for frame_line in frame:
        for i in range(len(word)):
            if i % 3 == 0:
                frame_word += wendy_frame[frame_line]
            else:
                frame_word += peterpan_frame[frame_line]
        frame_word += "\n"
    return frame_word

word = input()
print(create_frame(word, peterpan_frame))
