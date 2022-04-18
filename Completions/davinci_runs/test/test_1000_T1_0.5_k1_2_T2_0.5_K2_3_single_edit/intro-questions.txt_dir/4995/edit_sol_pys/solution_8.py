

# Workaround to input() in CodeForces
def read_ints():
    temp = input().split()
    temp_ints = [int(t) for t in temp]
    return temp_ints

def calculate_average_length_of_minute(minutes, seconds):
    return seconds / minutes

def main():
    observations = read_ints()[0]
    number_of_minutes_and_seconds = []
    for i in range(observations):
        number_of_minutes_and_seconds.append(read_ints())
    
    for i in number_of_minutes_and_seconds:
        average_length = calculate_average_length_of_minute(i[0], i[1])
        if average_length <= 1:
            print("measurement error")
        else:
            print(average_length)

if __name__ == "__main__":
    main()
