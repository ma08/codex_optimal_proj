

def min_length(n, words):  # n: 단어의 개수, words: 단어들을 리스트로 만들어줌
    count = 1  # 최소 길이는 적어도 1이어야 함.
    for i in range(n-1):  # 각 단어들을 비교해서 같지 않으면 count 증가
        if words[i] != words[i+1]:
            count += 1  # 만약 다음 단어들이 모두 같다면 count는 1이 된다.
    return count  # 최소 길이 반환

n = int(input())
words = input().split()
print(min_length(n, words))
