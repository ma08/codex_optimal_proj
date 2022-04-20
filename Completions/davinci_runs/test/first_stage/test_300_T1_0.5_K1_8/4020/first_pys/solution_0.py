

def main():
    time1 = input()
    time2 = input()
    time1_list = time1.split(':')
    time2_list = time2.split(':')
    time1_list = [int(i) for i in time1_list]
    time2_list = [int(i) for i in time2_list]
    time1_minutes = time1_list[0] * 60 + time1_list[1]
    time2_minutes = time2_list[0] * 60 + time2_list[1]
    midpoint = (time1_minutes + time2_minutes) / 2
    midpoint_hours = midpoint // 60
    midpoint_minutes = midpoint % 60
    if midpoint_hours < 10:
        midpoint_hours = '0' + str(midpoint_hours)
    else:
        midpoint_hours = str(midpoint_hours)
    if midpoint_minutes < 10:
        midpoint_minutes = '0' + str(midpoint_minutes)
    else:
        midpoint_minutes = str(midpoint_minutes)
    print(midpoint_hours + ':' + midpoint_minutes)

main()