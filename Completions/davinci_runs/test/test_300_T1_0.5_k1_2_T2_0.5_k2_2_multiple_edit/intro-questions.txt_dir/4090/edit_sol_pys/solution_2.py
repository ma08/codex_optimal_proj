
n = int(input())  # 입력받은 단어 수
words = input().split()  # 입력받은 단어들을 배열에 저장
def min_length(n, words):  # 가장 짧은 단어 길이 구하는 함수
    count = 1  # 서로 다른 단어의 수
    for i in range(n-1):  # 단어 수만큼 반복
        if words[i] != words[i+1]:  # 단어가 다르면
            count += 1  # 서로 다른 단어의 수 증가
    return count  # 서로 다른 단어의 수 반환
n = int(input())  # 입력받은 단어 수
words = input().split()  # 입력받은 단어들을 배열에 저장
print(min_length(n, words))  # 서로 다른 단어의 수 출력
