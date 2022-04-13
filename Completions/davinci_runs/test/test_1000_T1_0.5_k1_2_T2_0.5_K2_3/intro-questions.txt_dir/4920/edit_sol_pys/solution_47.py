

def get_input():
    return input()
    
def get_num_good_itineraries(events):
    start = None
    end = None
    for i in range(len(events)):
        if events[i][1] == "S":
            start = events[i]
        elif events[i][1] == "E":
            end = events[i]
    
    if start[0] == end[0]:
        return 0
    else:
        return 1

def main():
    events = get_input()
    good_itineraries = get_num_good_itineraries(events)
    print(good_itineraries)

if __name__ == "__main__":
    main()
