

# Workaround to input() in CodeForces
def read_ints():
    temp = input().split()
    temp_ints = [int(t) for t in temp]
    return temp_ints

def calculate_average_length_of_minute(number_of_minutes, seconds_elapsed):
    return seconds_elapsed / number_of_minutes

def main():
    number_of_observations = read_ints()[0]
    number_of_minutes_and_seconds_elapsed = []
    for i in range(number_of_observations):
        number_of_minutes_and_seconds_elapsed.append(read_ints())
    
    for i in number_of_minutes_and_seconds_elapsed:
        number_of_minutes = i[0]
        seconds_elapsed = i[1]
        average_length_of_minute = calculate_average_length_of_minute(number_of_minutes, seconds_elapsed)
        if average_length_of_minute <= 1:
            print("measurement error")
        else:
            print(average_length_of_minute)

if __name__ == "__main__":
    main()
