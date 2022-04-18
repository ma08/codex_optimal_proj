

# Workaround to input() in CodeForces
def read_ints():
    temp = input().split()
    temp_ints = [int(t) for t in temp]
    return temp_ints

def calculate_average_length_of_second(number_of_minutes, seconds):
    return seconds / number_of_minutes

def main():
    number_of_observations = read_ints()[0]
    number_of_minutes_and_seconds = []
    for i in range(number_of_observations):
        number_of_minutes_and_seconds.append(read_ints())
    
    for i in number_of_minutes_and_seconds:
        average_length_of_second = calculate_average_length_of_second(i[0], i[1])
        if average_length_of_second <= 1:
            print("measurement error")
        else:
            print(average_length_of_second)

if __name__ == "__main__":
    main()
