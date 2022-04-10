

import fileinput

def get_midpoint(start, end):
    # Get the total number of minutes
    total_min = (end[0] - start[0]) * 60 + (end[1] - start[1])
    # Add half of the number of minutes to the start time
    midpoint = [start[0], start[1] + (total_min / 2)]
    # If the time rolled over to the next hour, adjust the hour
    if midpoint[1] >= 60:
        midpoint[1] -= 60
        midpoint[0] += 1
        if midpoint[0] == 24:
            midpoint[0] = 0
    # If the minutes are less than 10, prepend a zero
    if midpoint[1] < 10:
        midpoint[1] = '0' + str(midpoint[1])
    else:
        midpoint[1] = str(midpoint[1])
    # If the hours are less than 10, prepend a zero
    if midpoint[0] < 10:
        midpoint[0] = '0' + str(midpoint[0])
    else:
        midpoint[0] = str(midpoint[0])
    # Return the midpoint
    return ':'.join(midpoint)

def main():
    # Read in the input
    start_time = fileinput.input()[0].split(':')
    end_time = fileinput.input()[0].split(':')
    start_time = [int(start_time[0]), int(start_time[1])]
    end_time = [int(end_time[0]), int(end_time[1])]
    # Call the function
    print(get_midpoint(start_time, end_time))

if __name__ == '__main__':
    main()
