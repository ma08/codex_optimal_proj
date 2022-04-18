# 프로그래머스 인턴십 코딩테스트 연습문제
# 자동완성
# https://programmers.co.kr/learn/courses/30/lessons/17685

def solution(words):
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = True
    return trie

def solution2(words):
    words = list(set(words))
    words.sort()
    answer = 0
    for word in words:
        answer += len(word) + 1
        for i in range(1, len(word)):
            if word[:i] in words:
                answer -= 1
                break
    return answer

words = ["go", "gone", "guild"]
print(solution(words), solution2(words))

words = ["abc", "def", "ghi", "jklm"]
print(solution(words), solution2(words))

words = ["word", "war", "warrior", "world"]
print(solution(words), solution2(words))
