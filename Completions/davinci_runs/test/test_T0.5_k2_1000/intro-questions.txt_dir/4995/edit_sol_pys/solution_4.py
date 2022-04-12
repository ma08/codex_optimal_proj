

# Workaround to input() in Code Forces
def read_ints(number_of_inputs):
    return [int(input()) for i in range(number_of_inputs)]

def calculate_average_length_of_minute(number_of_minutes, seconds):
    return seconds / number_of_minutes

def main():
    number_of_observations = read_ints(1)[0]
    number_of_minutes_and_seconds = []
    for i in range(number_of_observations):
        number_of_minutes_and_seconds.append(read_ints())
    
    for i in number_of_minutes_and_seconds:
        average_length_of_minute = calculate_average_length_of_minute(i[0], i[1])
        if average_length_of_minute <= 1:
            print("measurement error")
        else:
            print(average_length_of_minute)

if __name__ == "__main__":
    main()
