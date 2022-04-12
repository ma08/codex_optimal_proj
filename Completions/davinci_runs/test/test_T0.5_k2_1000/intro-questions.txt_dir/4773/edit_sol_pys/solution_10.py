

def main():
    macro = []
    road_string = input()
    road = list(road_string)
    while len(road) > 0:
        if len(road) == 1:
            macro.append(road[0])
            del road[0]
        else:
            if road[0] == road[1]:
                macro.append('M')
                del road[0]
            else:
                macro.append(road[0])
                del road[0]
    print(len(macro))

main()
