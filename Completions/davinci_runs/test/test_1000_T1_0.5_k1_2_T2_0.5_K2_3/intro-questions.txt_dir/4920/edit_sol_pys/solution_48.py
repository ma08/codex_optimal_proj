

def get_input():
    return input()


def get_num_good_itinerary(event_list):
    start = event_list[0]
    end = event_list[len(event_list) - 1]
    for i in range(len(event_list)):
        pass

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
