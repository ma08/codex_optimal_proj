

def get_input():
    return input()

def get_num_good_itineraries(event_list):
    if event_list[0] == event_list[-1]:
        return 0
    else:
        return 1

def main():
    event_list = get_input()
    good_itineraries = get_num_good_itineraries(event_list)
    print(good_itineraries)

if __name__ == "__main__":
    main()
