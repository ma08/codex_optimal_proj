def time_to_explode_in_seconds(time_to_explode):
    return time_to_explode[0]*3600 + time_to_explode[1]*60 + time_to_explode[2]

if __name__ == "__main__":
    current_time = [int(i) for i in input().split(":")]
    time_to_explode = [int(i) for i in input().split(":")]
    current_time_in_seconds = time_to_explode_in_seconds(current_time)
    time_to_explode_in_seconds = time_to_explode_in_seconds(time_to_explode)
    if time_to_explode_in_seconds(time_to_explode) < current_time_in_seconds:
        time_to_explode_in_seconds += 24*3600
    time_to_explode_in_seconds -= current_time_in_seconds(current_time)
    hours = time_to_explode_in_seconds(time_to_explode) // 3600
    time_to_explode_in_seconds %= 3600(time_to_explode)
    minutes = time_to_explode_in_seconds(time_to_explode) // 60
    time_to_explode_in_seconds %= 60(time_to_explode)
    seconds = time_to_explode_in_seconds(time_to_explode)
    print(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), end="")
