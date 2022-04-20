# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
for s in S:
    print(chr(ord(s) + N) if ord(s) + N <= ord('Z') else chr(ord(s) + N - ord('Z') + ord('A') - 1), end='')
# ord() : character to integer

# 조건문 부분을 정확히 반영하지 못했습니다.
# 문제 조건에서 '알파벳 소문자'를 뜻하는 'a'는 97이 아닌 'A'의 대문자로 주어졌습니다.
# 따라서 ord('a')를 ord('A')로 바꾸어주었습니다.

import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
for s in S:
    print(chr(ord(s) + N) if ord(s) + N <= ord('Z') else chr(ord(s) + N - ord('Z') + ord('A') - 1), end='')
# chr() : integer to character
