

def get_input():
    return input().split()

def get_num_good_itineraries(event_list):
    start = None
    end = None
    start = event_list[0]
    end = event_list[-1]
    if start == end:
        return 0
    else:
        return 1

def main():
    event_list = get_input()
    print(event_list)
    good_itineraries = get_num_good_itineraries(event_list)
    print(good_itineraries)

if __name__ == "__main__":
    main()
