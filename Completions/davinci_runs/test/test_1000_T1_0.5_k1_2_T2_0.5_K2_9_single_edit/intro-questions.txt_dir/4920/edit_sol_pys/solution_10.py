

def get_itinerary_list():
    return input().split(",")

def get_num_good_itineraries(itinerary_list):
    return len(itinerary_list) - 1

def main():
    itinerary_list = get_itinerary_list()
    good_itineraries = get_num_good_itineraries(itinerary_list)
    print(good_itineraries)

if __name__ == "__main__":
    main()
