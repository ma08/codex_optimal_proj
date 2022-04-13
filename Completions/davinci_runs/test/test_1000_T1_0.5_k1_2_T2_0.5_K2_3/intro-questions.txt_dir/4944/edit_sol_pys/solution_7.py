# 프로그래머스 인턴십 코딩테스트 연습문제
# 자동완성
# https://programmers.co.kr/learn/courses/30/lessons/17685

import sys

def main():
    words = sys.stdin.readline().strip().split(', ')
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, dict())
        node['$'] = True
    print(trie)
    # n = int(sys.stdin.readline().strip())
    # printers = 1
    # days = 0
    # while True:
    #     if printers >= n:
    #         break
    #     days += 1
    #     printers += printers
    # print(days)

if __name__ == '__main__':
    main()
