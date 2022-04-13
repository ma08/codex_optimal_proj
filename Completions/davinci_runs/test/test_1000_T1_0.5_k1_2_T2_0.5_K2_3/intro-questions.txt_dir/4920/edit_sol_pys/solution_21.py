

def get_input():
    return input().split()

def get_num_good_itineraries(events):
    start = None
    end = None
    start = events[0]
    end = events[len(events) - 1]
    
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
