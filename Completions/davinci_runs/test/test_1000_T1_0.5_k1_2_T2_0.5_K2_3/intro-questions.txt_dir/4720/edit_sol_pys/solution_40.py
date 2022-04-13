# Solved by myself

# 이런 문제가 있었네.
# 이건 내가 짠 코드.
# 입력받은 리스트를 길이가 짧은 순서대로 정렬하고,
# 이전 좌석의 끝과 현재 좌석의 시작을 비교하면서
# 중복되는 부분이 있다면, 그 부분을 제외한 칸 수를 더하면 된다.

N = int(input())

seat_list = []

for i in range(N):
    seat_list.append(list(map(int, input().split())))

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
