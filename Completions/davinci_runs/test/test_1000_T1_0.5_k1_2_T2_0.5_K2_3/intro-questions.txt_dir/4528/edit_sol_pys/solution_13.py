#시간차를 구하는 문제

t = int(input())

for i in range(t):
    h, m = map(int, input().split()) #시간과 분을 받아서 정수형으로 변환하여 h, m에 넣는다.
    print(1440 - (h * 60 + m)) #입력받은 시간과 분을 분으로 변환하여 전체 분에서 빼준다.
