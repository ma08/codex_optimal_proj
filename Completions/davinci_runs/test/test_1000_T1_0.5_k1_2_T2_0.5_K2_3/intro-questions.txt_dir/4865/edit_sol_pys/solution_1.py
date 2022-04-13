

def time_to_int(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)



def int_to_time(seconds):
    time = "00:00"
    return time[:-len(str(seconds % 60))] + str(seconds % 60) + ":" + time[:-len(str(seconds // 60))] + str(
        seconds // 60)


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def main():
    print(add_time("3:45", "3:30"))


if __name__ == '__main__':
    main()
