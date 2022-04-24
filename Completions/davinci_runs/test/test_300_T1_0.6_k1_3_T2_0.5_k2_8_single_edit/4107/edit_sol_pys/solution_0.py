
import bisect

def solution(n, k, s):
    # create a list of rooms which have router
    rooms_with_router = [i + 1 for i, room in enumerate(s) if room == '1']

    # rooms to check
    rooms_to_check = [i + 1 for i, room in enumerate(s) if room == '0']

    # total cost
    cost = 0

    # for each room to check
    for room in rooms_to_check:

        # if room has router, skip
        if room in rooms_with_router:
            continue

        # if room is the first room
        if room == 1:
            # set the closest router to the right
            closest_router = rooms_with_router[0]

            # if the closest router is out of range, the room needs to be connected directly
            if closest_router > room + k:
                cost += room
            # else, the room is connected to the internet
            else:
                pass

        # if room is the last room
        elif room == n:
            # set the closest router to the left
            closest_router = rooms_with_router[-1]

            # if the closest router is out of range, the room needs to be connected directly
            if closest_router < room - k:
                cost += room
            # else, the room is connected to the internet
            else:
                pass

        # if room is in between first and last room
        else:
            # set the closest router to the left
            closest_router_left = rooms_with_router[bisect.bisect_right(rooms_with_router, room) - 1]

            # set the closest router to the right
            closest_router_right = rooms_with_router[bisect.bisect_left(rooms_with_router, room)]

            # if both routers are out of range, the room needs to be connected directly
            if closest_router_left < room - k and closest_router_right > room + k:
                cost += room
            # else, the room is connected to the internet
            else:
                pass

    return cost


print(solution(5, 2, '00100'))
print(solution(6, 1, '000000'))
print(solution(4, 1, '0011'))
print(solution(12, 6, '000010000100'))  # 3
