

def main():
    macro = []
    road = []
    road_string = raw_input()
    road_len = len(road_string)
    for i in range(road_len):
        road.append(road_string[i])
    while len(road) > 0:
        if len(road) == 1:
            macro.append(road[0])
            del road[0]
        else:
            if road[0] == road[1]:
                macro.append('M')
                del road[0]
                del road[0]
            else:
                macro.append(road[0])
                del road[0]
    print(len(macro))

main()
