

if __name__ == "__main__":
    current_time = [int(i) for i in input().split(":")]
    time_to_explode = [int(i) for i in input().split(":")]
    current_time_in_seconds = current_time[0] * 3600 + current_time[1] * 60 + current_time[2]
    time_to_explode_in_seconds = time_to_explode[0] * 3600 + time_to_explode[1] * 60 + time_to_explode[2]
    if time_to_explode_in_seconds <= current_time_in_seconds:
        time_to_explode_in_seconds += 24 * 3600
    time_to_explode_in_seconds -= current_time_in_seconds  # get remaining time
    hours = time_to_explode_in_seconds // 3600  # get hours
    time_to_explode_in_seconds %= 3600  # get remaining time
    minutes = time_to_explode_in_seconds // 60  # get minutes
    time_to_explode_in_seconds %= 60  # get remaining time
    seconds = time_to_explode_in_seconds  # get seconds
    print(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
