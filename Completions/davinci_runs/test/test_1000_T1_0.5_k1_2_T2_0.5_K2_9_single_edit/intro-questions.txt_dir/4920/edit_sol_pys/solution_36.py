

def get_input():
    return input()

def get_num_good_itineraries(events):
    start = None
    end = None
    for i in range(len(events)):
        if i == 0:
            start = events[i]
        elif i == len(events) - 1:
            end = events[i]
    
    if start == end:
        return 0
    else:
        return 1

def main():
    events = get_input()
    good_itineraries = get_num_good_itineraries(events)
    print(good_itineraries)

if __name__ == "__main__":
    main()
