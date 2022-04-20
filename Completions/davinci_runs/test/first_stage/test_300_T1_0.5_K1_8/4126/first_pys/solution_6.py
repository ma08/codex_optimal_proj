

# A string S of an odd length is said to be a strong palindrome if and only if all of the following conditions are satisfied:
#  - S is a palindrome.
#  - Let N be the length of S. The string formed by the 1-st through ((N-1)/2)-th characters of S is a palindrome.
#  - The string consisting of the (N+3)/2-st through N-th characters of S is a palindrome.

# Determine whether S is a strong palindrome.

# -----Constraints-----
#  - S consists of lowercase English letters.
#  - The length of S is an odd number between 3 and 99 (inclusive).

# -----Input-----
# Input is given from Standard Input in the following format:
# S

# -----Output-----
# If S is a strong palindrome, print Yes;
# otherwise, print No.

# -----Sample Input-----
# akasaka

# -----Sample Output-----
# Yes

#  - S is akasaka.
#  - The string formed by the 1-st through the 3-rd characters is aka.
#  - The string formed by the 5-th through the 7-th characters is aka.
# All of these are palindromes, so S is a strong palindrome.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  IkaLog
#  ======
#  Copyright (C) 2015 Takeshi HASEGAWA
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import sys
import cv2

# Returns True if the specified image is blank.
def is_blank_image(img):
    if img is None:
        return True

    if img.size == 0:
        return True

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_b = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #print('img_b.shape %s %s' % (img_b.shape[0], img_b.shape[1]))
    if (img_b.shape[0] * img_b.shape[1] == 0):
        return True

    if (img_b.shape[0] == 1) and (img_b.shape[1] == 1):
        return True

    return False

def is_palindrome(line):
    line_len = len(line)
    for i in range(0, line_len):
        if line[i] != line[line_len - i - 1]:
            return False
    return True

def is_strong_palindrome(line):
    line_len = len(line)
    if (line_len % 2) == 0:
        return False
    if not is_palindrome(line):
        return False
    if not is_palindrome(line[0:int(line_len / 2)]):
        return False
    if not is_palindrome(line[int((line_len + 3) / 2) - 1:line_len]):
        return False

    return True

if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    if is_strong_palindrome(line):
        print('Yes')
    else:
        print('No')