

def get_input():
    return input()

def get_num_good_itineraries(event_list, num_events):
    start = None
    end = None
    for i in range(num_events):
        if i == 0:
            start = event_list[i]
        elif i == num_events - 1:
            end = event_list[i]
    
    if start == end:
        return 1
    else:
        return 0

def main():
    event_list = list(get_input())
    num_events = len(event_list)
    good_itineraries = get_num_good_itineraries(event_list, num_events)
    print(good_itineraries)

if __name__ == "__main__":
    main()
