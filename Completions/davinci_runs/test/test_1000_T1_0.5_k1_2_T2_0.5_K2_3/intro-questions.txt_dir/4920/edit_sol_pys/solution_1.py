

def get_input():
    return list(input())

def get_num_good_itinerary(event_list):
    start = None
    end = None
    for i in range(len(event_list)):
        if i == 0:
            start = event_list[i]
        elif i == len(event_list) - 1:
            end = event_list[i]
    
    if start == end:
        return 0
    else:
        return 1

def main():
    event_list = get_input()
    good_itinerary = get_num_good_itinerary(event_list)
    print(good_itinerary)

if __name__ == "__main__":
    main()
