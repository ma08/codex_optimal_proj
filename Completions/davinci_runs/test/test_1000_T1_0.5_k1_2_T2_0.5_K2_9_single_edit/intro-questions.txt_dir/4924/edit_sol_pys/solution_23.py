


if __name__ == "__main__":
    current_time = [int(i) for i in input().split(":")]
    time_to_explode = [int(i) for i in input().split(":")]
    current_time_in_seconds = current_time[0]*3600 + current_time[1]*60 + current_time[2]
    time_to_explode_in_seconds = time_to_explode[0]*3600 + time_to_explode[1]*60 + time_to_explode[2]
    if time_to_explode_in_seconds < current_time_in_seconds:
        time_to_explode_in_seconds += 24*3600
    time_to_explode_in_seconds -= current_time_in_seconds
    hours = time_to_explode_in_seconds // 3600
    time_to_explode_in_seconds %= 3600
    minutes = time_to_explode_in_seconds // 60
    time_to_explode_in_seconds %= 60
    seconds = time_to_explode_in_seconds
    print(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
