
def solution(n, k, s):
    # create a list of rooms which have a router
    rooms_with_router = [i + 1 for i, room in enumerate(s) if room == '1']

    # rooms without a router
    rooms_without_router = [i + 1 for i, room in enumerate(s) if room == '0']

    # total cost
    cost = 0

    # for each room without a router
    for room in rooms_without_router:

        # if room is the first room (1)
        if room == 1:
            # set the closest router to the right (2)
            closest_router = rooms_with_router[0]

            # if the closest router is out of range, the room needs to be connected directly (3)
            if closest_router > room + k:
                cost += room
            # else, the room is connected to the internet (4)
            else:
                pass

                pass

        # if room is the last room (5)
        elif room == n:
            # set the closest router to the left (6)
            closest_router = rooms_with_router[-1]

            # if the closest router is out of range, the room needs to be connected directly (7)
            if closest_router < room - k:
                cost += room
            # else, the room is connected to the internet (8)
            else:
                pass

                pass

        # if room is in between first and last room (9)
        else:
            # set the closest router to the left (10)
            closest_router_left = rooms_with_router[bisect.bisect_right(rooms_with_router, room) - 1]

            # set the closest router to the right (11)
            closest_router_right = rooms_with_router[bisect.bisect_left(rooms_with_router, room)]

            # if both routers are out of range, the room needs to be connected directly (12)
            if closest_router_left < room - k and closest_router_right > room + k:
                cost += room
                pass
            # else, the room is connected to the internet (13)
            else:
                pass

    return cost


print(solution(5, 2, '00100'))
print(solution(6, 1, '000000'))
print(solution(4, 1, '0011'))
print(solution(12, 6, '000010000100'))
