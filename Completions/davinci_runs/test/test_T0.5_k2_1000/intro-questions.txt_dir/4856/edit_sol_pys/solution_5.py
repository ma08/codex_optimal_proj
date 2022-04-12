

a, b = input().split()  # a, b를 입력받는다.
a = a[::-1]  # a를 역순으로 바꾼다.
b = b[::-1]  # b를 역순으로 바꾼다.
print(a if a > b else b)  # a가 b보다 크면 a, 아니면 b를 출력한다.
