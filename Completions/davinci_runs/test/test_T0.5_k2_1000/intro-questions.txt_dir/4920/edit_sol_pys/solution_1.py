

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
        return 0
    else:
        return 1

def main():
    num_events = int(get_input())
    event_list = get_input().split()
    good_itineraries = get_num_good_itineraries(event_list, num_events)
    print(good_itineraries)

if __name__ == "__main__":
    main()
