

# Workaround to input() in CodeForces
def read_ints():
    temp_ints = input().split()
    temp_ints = [int(i) for i in temp_ints]
    return temp_ints

def calculate_average_length_of_minute(number_of_minutes, seconds) -> int:
    return seconds / number_of_minutes

def main():
    number_of_observations = read_ints()
    number_of_observations = number_of_observations[0]
    number_of_minutes_and_seconds = [[]]
    for i in range(number_of_observations):
        number_of_minutes_and_seconds[i] = read_ints()
    
    for i in number_of_minutes_and_seconds:
        average_length_of_minute = calculate_average_length_of_minute(i[1], i[0])
        print(average_length_of_minute)
        if average_length_of_minute < 1:
            print("measurement error")
        else:
            print(average_length_of_minute)

if __name__ == "__main__":
    main()
