
N = int(input())

seat_list = []

for i in range(N):
    seat_list.append(list(map(int, input().split())))   # map(함수, 자료구조) : 자료구조의 모든 원소를 함수에 적용한 결과를 묶어서 반환

seat_list.sort(key=lambda x: x[0])

count = 0

for i in range(N):
    if i == 0:
        count += seat_list[i][1] - seat_list[i][0] + 1
    else:
        if seat_list[i][0] <= seat_list[i-1][1]:
            if seat_list[i][1] > seat_list[i-1][1]:
                count += seat_list[i][1] - seat_list[i-1][1]
        else:
            count += seat_list[i][1] - seat_list[i][0] + 1

print(count)
