#!/usr/bin/env python

import sys
import os
import re



def is_binary(filename):
    """Return true if the given filename appears to be binary.
    File is considered to be binary if it contains a NULL byte.
    FIXME: This approach incorrectly reports UTF-16 as binary.
    """
    with open(filename, 'rb') as f:
        for block in f:
            if '\0' in block:
                return True
    return False


def is_text_file(filename):
    import mimetypes
    return mimetypes.guess_type(filename)[0] == 'text/plain'


def is_image_file(filename):
    import mimetypes
    return mimetypes.guess_type(filename)[0] in ['image/jpeg', 'image/png']


def is_music_file(filename):
    import mimetypes
    return mimetypes.guess_type(filename)[0] in ['audio/mpeg', 'audio/mp4']


def is_video_file(filename):
    import mimetypes
    return mimetypes.guess_type(filename)[0] in ['video/mp4']




def main():
    print is_text_file('text.txt')
    print is_text_file('text.pdf')
    print is_image_file('image.jpg')
    print is_image_file('image.txt')
    print is_music_file('music.mp3')
    print is_music_file('music.txt')
    print is_video_file('video.mp4')
    print is_video_file('video.txt')


if __name__ == '__main__':
    main()
