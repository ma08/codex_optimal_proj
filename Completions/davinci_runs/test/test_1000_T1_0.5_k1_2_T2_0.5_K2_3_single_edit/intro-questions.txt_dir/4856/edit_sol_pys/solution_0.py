
a, b = input().split()  # a,b를 입력받고 공백을 기준으로 분리해줍니다.
a = a[::-1]  # a를 뒤집어줍니다.
b = b[::-1]  # b를 뒤집어줍니다.
print(a if a > b else b)  # a가 크면 a를 출력하고 그렇지 않으면 b를 출력합니다.
