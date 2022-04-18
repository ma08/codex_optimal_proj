
def min_length(n, words):
    count = 1  # 최소 길이는 적어도 1이어야 함
    for i in range(n-1):
        if words[i] != words[i+1]:  # 이전 단어와 다음 단어가 다르면 count 증가
            count += 1
    return count

n = int(input())  # 단어의 개수
words = input().split()  # 단어들을 리스트로 만들어줌

print(min_length(n, words))
