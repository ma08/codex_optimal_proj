

# Solved by myself 

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
