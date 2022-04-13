

def get_input():
    return int(input())

def get_num_good_itineraries(num_events):
    return num_events - 1
    

def main():
    num_events = get_input()
    good_itineraries = get_num_good_itineraries(num_events)
    print(good_itineraries)

if __name__ == "__main__":
    main()
